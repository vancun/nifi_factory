from jinja2 import Environment, FileSystemLoader, Template
from os import path
import argparse
import logging
import sys
import json


class Jinja2Render:

    def __init__(self):
        self._initArgs()
        self._initLogger()
        self._log.debug('*** Started: {}'.format(sys.argv))
        self._log.debug('Parsed args: {}'.format(self._args))
        self._initModel()

    @property
    def log(self):
        return self._log

    def _initLogger(self):
        level = getattr(logging, self._args.log)
        logger = logging.getLogger(type(self).__name__)
        logger.setLevel(level)

        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        self._log = logger

    def _initArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('template', nargs='*', default='-',
                            help="Templates to render. Use STDIN if not specified")
        parser.add_argument('--path', action='append',
                            help='Template search path.')
        parser.add_argument('-v', '--var', action='append',
                            help='Add variable to the model.')
        parser.add_argument('-m', '--model', action='append',
                            help='Add model.')
        parser.add_argument(
            '--log', choices=['ERROR', 'WARNING', 'DEBUG', 'INFO', 'DEBUG'], default='INFO', help='Log level. Default: INFO')
        self._args = parser.parse_args()

    def _loadJsonFiles(self):
        if (self._args.model):
            for js_file in self._args.model:
                *names, filename = js_file.split('=', 2)
                with open(filename, 'r') as f:
                    value = json.load(f)
                if (names):
                    name = names[0]
                    self._model[name] = value
                    self.log.debug('Model loaded from JSON file {} into {}: {}'.format(
                        filename, name, value))
                else:
                    self._model.update(value)
                    self.log.debug(
                        'Model merged from JSON file {}: {}'.format(filename, value))

    def _initModel(self):
        model = dict((v.split('=', 2)
                      for v in self._args.var)) if self._args.var else {}
        self._model = model
        self.log.debug('Model initialized: {}'.format(self._model))
        self._loadJsonFiles()
        self.log.debug('Model: {}'.format(self._model))

    def _render_from_file(self, file_name):
        self._log.debug('Rendering file {}.'.format(file_name))
        search_path = list(self._args.path) if self._args.path else[]
        search_path.append(path.dirname(file_name))
        self._log.debug('Effective search path {}.'.format(search_path))
        loader = FileSystemLoader(search_path)
        env = Environment(loader=loader)
        template = env.get_template(path.basename(file_name))
        return template.render(self._model)

    def run(self):
        for file_name in self._args.template:
            print(self._render_from_file(file_name))


if __name__ == "__main__":
    Jinja2Render().run()
