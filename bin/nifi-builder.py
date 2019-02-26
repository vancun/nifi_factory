# import json
import argparse
from nifi import *
import logging
import sys


class NiFiBuildContext:

    def __init__(self, nifi, pipeline_def):
        self._nifi = nifi
        self._pipeline_def = pipeline_def
        self._pipeline_pg = None
        self._steps = list()
        logging.basicConfig(level=logging.DEBUG)
        self._log = logging.getLogger('nifibuilder')
        self._load_templates()

    @property
    def log(self):
        return self._log

    @property
    def templates(self):
        return self._templates

    @property
    def pipeline_pg(self):
        return self._pipeline_pg

    @property
    def steps(self):
        return self._steps

    @pipeline_pg.setter
    def pipeline_pg(self, value):
        self._pipeline_pg = value

    @property
    def pipeline(self):
        return self._pipeline_def

    @property
    def nifi(self):
        return self._nifi

    def _load_templates(self):
        self._templates = {}
        for tpl in self._nifi.get_templates()['templates']:
            self._templates[tpl['template']['name']] = tpl


class NiFiBuilder:
    _params = {
        'v_space': 300,
        'h_space': 570  # 380 is PG width
    }

    def __init__(self, params):
        self._params.update(params)
        self._connect()

    def _connect(self):
        self._nifi = NiFiClient(self._params['nifi_url'])

    def _find_default_pos(self):
        """Find position for a new process group.

        Returns (x,y) pair."""
        pg = self._nifi.get_process_group(self._nifi.root_id)
        x, y = 0, 0
        flow = pg['processGroupFlow']['flow']
        positions = []
        for entity in ('processGroups', 'remoteProcessGroups', 'processors', 'inputPorts', 'outputPorts', 'funnels'):
            print(entity)
            positions.extend(item['position'] for item in flow[entity])
        x = min(positions, key=lambda pos: pos['x'])['x']
        y = max(positions, key=lambda pos: pos['y'])['y']
        return (x, y + self._params['v_space'])

    def _find_root_pg_by_name(self, name):
        """Search for a process group at root level by name.

        Returns a process group descriptor or None. In case multiple
        results are found, an exception is raised."""
        parent_id = self._nifi.root_id
        parent_group = self._nifi.get_process_group(parent_id)
        pg_list = parent_group['processGroupFlow']['flow']['processGroups']
        results = list(
            filter(lambda pg: pg['component']['name'] == name, pg_list))
        if len(results) > 1:
            raise Exception(
                "Multiple ({}) process groups named {} exist.".format(len(results), name))
        elif len(results) == 1:
            return results[0]
        else:
            return None

    def _create_or_replace_pipeline_pg(self, ctx):
        """Ensure root process group for the pipeline exists."""
        pg = self._find_root_pg_by_name(ctx.pipeline.name)
        if (pg):
            pos_x = pg['component']['position']['x']
            pos_y = pg['component']['position']['y']
            #ctx.pipeline_pg = pg
            # return
            self._nifi.delete_process_group(
                pg['id'], pg['revision']['version'])
            ctx.log.info('Existing pg {id} deleted'.format(id=pg['id']))
        else:
            pos_x, pos_y = self._find_default_pos()
        pg = self._nifi.create_process_group(ctx.pipeline.name,
                                             self._nifi.root_id, pos_x, pos_y)
        ctx.pipeline_pg = NiFiProcessGroup(pg)
        if ctx.pipeline.description:
            self._nifi.configure_pg(
                ctx.pipeline_pg.id, comments=ctx.pipeline.description)
        ctx.log.debug('Created pg {id}'.format(id=ctx.pipeline_pg.id))

    def _update_pg_vars(self, pg_id, vars, ctx):
        # Get current vars
        current_vars = ctx.nifi.get_pg_vars(pg_id)
        new_vars = {}
        for v in current_vars['variableRegistry']['variables']:
            new_vars[v['variable']['name']] = v['variable']['value']
        for v in vars:
            if vars[v] is None:
                if v in new_vars:
                    new_vars.pop(v)
                continue
            new_vars[v] = vars[v].format_map(ctx.pipeline.parameters)
        ctx.nifi.update_pg_vars(pg_id, new_vars)

    def _add_steps(self, ctx):
        x_pos = 0
        y_pos = 0
        for step in ctx.pipeline.steps:
            result = ctx.nifi.instantiate_template(ctx.pipeline_pg.id,
                                                   ctx.templates[step.step_type]['id'],
                                                   x_pos,
                                                   y_pos)
            pg = result['flow']['processGroups'][0]
            flow_pg = NiFiProcessGroupFlow(
                ctx.nifi.get_process_group(pg['id']))
            ctx.steps.append(flow_pg)
            x_pos += self._params['h_space']
            ctx.nifi.configure_pg(
                flow_pg.id, name=step.name, comments=step.description)
            self._update_pg_vars(flow_pg.id, step.variables, ctx)

    def _add_connection(self, ctx, src, dest):
        link = {
            "name": "auto-link",
            "source": {
                "id": src.id,
                "groupId": src.group_id,
                "type": "OUTPUT_PORT"
            },
            "destination": {
                "id": dest.id,
                "groupId": dest.group_id,
                "type": "INPUT_PORT"
            }
        }
        ctx.nifi.add_connection(ctx.pipeline_pg.id, link)

    def _add_connections(self, ctx):
        prev_step = None
        for this_step in ctx.steps:
            if prev_step is None:
                prev_step = this_step
                continue
            src_port = prev_step.get_outport('out')
            dest_port = this_step.get_inport('in')
            self._add_connection(ctx, src_port, dest_port)
            prev_step = this_step

    def build(self, pipeline_def):
        ctx = NiFiBuildContext(self._nifi, pipeline_def)
        self._create_or_replace_pipeline_pg(ctx)
        self._add_steps(ctx)
        self._add_connections(ctx)


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='NiFi Flow Builder')
    parser.add_argument('-u', '--nifi-url', default='http://localhost:8080',
                        help='URL for the NiFi server. Default URL: http://localhost:8080')
    parser.add_argument('-o', '--overwrite', action='store_true',
                        help='Overwrite existing pipeline.')
    # parser.add_argument('-p', '--properties', action='append', help='Properties file.')
    parser.add_argument('filename')
    return parser.parse_args(args)


if (__name__ == "__main__"):
    import os

    args = parse_args()

    with open(args.filename) as pipeline_file:
        # pipeline = DataPipeline.from_descriptor(json.load(pipeline_file))
        pipeline = DataPipelineFactory.from_json_file_descriptor(pipeline_file)

    builder = NiFiBuilder(args.__dict__)
    builder.build(pipeline)
