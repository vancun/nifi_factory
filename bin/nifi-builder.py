#! /usr/bin/python3
import argparse
from nifi import *
import logging
import sys
import json


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

    @property
    def options(self):
        return self._params

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
            positions.extend(item['position'] for item in flow[entity])
        if positions:
            x = min(positions, key=lambda pos: pos['x'])['x']
            y = max(positions, key=lambda pos: pos['y'])['y']
            y += self._params['v_space']
        return (x, y)

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
		

    def _find_child_pg_by_name(self, name, parent_id=None):
        if parent_id is None:
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
            
    def _find_processor_by_path(self, path):
        """Find and return processor info by path"""
        parent_id = self._nifi.root_id
        path_elements = path.split('/')
        for pg_name in path_elements[:-1]:
            pg = self._find_child_pg_by_name(pg_name, parent_id)
            if not pg:
                raise Exception("Process group {} not found in path {}.".format(pg_name, path))
            pg_id = pg['id']
            print("Search for: {}. Found: {}".format(pg_name, pg_id))
            parent_id = pg_id
        pg = self._nifi.get_process_group(parent_id)
        processor_list = pg['processGroupFlow']['flow']['processors']
        processor_name = path_elements[-1]
        results = list(
            filter(lambda pg: pg['component']['name'] == processor_name, processor_list))
        if not results:
            raise Exception('Processor {} not found in path: {}'.format(processor_name, path))
        elif len(results) > 1:
            raise Exception('Multiple processors {} found in path: {}'.format(processor_name, path))
        return results[0]

    def _create_or_replace_pipeline_pg(self, ctx):
        """Ensure root process group for the pipeline exists."""
        pg = self._find_root_pg_by_name(ctx.pipeline.name)
        if (pg and not self.options['overwrite']):
            raise Exception(
                "Pipeline process group {} already exists. Consider --overwrite option.".format(ctx.pipeline.name))
        if (pg):
            pos_x = pg['component']['position']['x']
            pos_y = pg['component']['position']['y']
            # ctx.pipeline_pg = pg
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

    def _update_pg_vars(self, pg_id, var_spec, ctx):
        new_vars = {}
        for v in var_spec:
            new_vars[v] = None if (var_spec[v] is None) else var_spec[v].format_map(
                ctx.pipeline.parameters)
        ctx.log.debug(
            "Update variables for {} with {}".format(pg_id, new_vars))
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
			
    def _update_properties(self, ctx):
        for path, props in ctx.pipeline.properties.items():
            processor = self._find_processor_by_path(path)
            proc_id = processor['component']['id']
            proc_version = processor['revision']['version']
            new_props = {}
            for n,v in props.items():
                new_props[n] = None if (v is None) else v.format_map(
                    ctx.pipeline.parameters)
            self._nifi.update_processor_properties(proc_id, new_props, proc_version)
        # print(ctx.pipeline.properties)

    def build(self, pipeline_def, conf):
        ctx = NiFiBuildContext(self._nifi, pipeline_def)
        self._create_or_replace_pipeline_pg(ctx)
        self._update_pg_vars(ctx.pipeline_pg.id, pipeline_def.variables, ctx)
        self._add_steps(ctx)
        self._add_connections(ctx)
        self._update_properties(ctx)


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='NiFi Flow Builder')
    parser.add_argument('-u', '--nifi-url', default='http://localhost:8080',
                        help='URL for the NiFi server. Default URL: http://localhost:8080')
    parser.add_argument('-c', '--config-file',
                        help='Additional json configuration file.')
    parser.add_argument('-o', '--overwrite', action='store_true',
                        help='Overwrite existing pipeline.')
    parser.add_argument('--bind-port')
    # parser.add_argument('-p', '--properties', action='append', help='Properties file.')
    parser.add_argument('filename')
    return parser.parse_args(args)

from flask import Flask, jsonify, request, send_from_directory, render_template, url_for
http_app = Flask(__name__)

def http_error(error=None):
    message = {
            'status': 500,
            'message': error,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

@http_app.route('/build', methods=['GET', 'POST'])
def http_build():
    try:
        builder = NiFiBuilder(args.__dict__)
        builder.build(pipeline, conf)
        message = {
            'status': 200,
            'message': 'Build pipeline "{}" complete.'.format(pipeline.name)
        }
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as ex:
        return http_error(format(ex))


if (__name__ == "__main__"):
    import os

    args = parse_args()

    with open(args.filename) as pipeline_file:
        # pipeline = DataPipeline.from_descriptor(json.load(pipeline_file))
        pipeline = DataPipelineFactory.from_json_file_descriptor(pipeline_file)

    if args.config_file:
        with open(args.config_file) as conf_file:
            conf = json.load(conf_file)
    else:
        conf = { 'parameters': {} }

    pipeline.parameters.update(conf['parameters'])
        
    if args.bind_port:
            http_app.run(debug=True, host='0.0.0.0', port=args.bind_port)
    else:
        try:
            builder = NiFiBuilder(args.__dict__)
            builder.build(pipeline, conf)
        except Exception as ex:
            print("ERROR: {}".format(ex), file=sys.stderr)
            # logging.exception(ex)
