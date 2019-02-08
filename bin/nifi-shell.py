import click
import requests
import re
import cmd
import json

class VancunNiFiClient:
    
    def __init__(self, nifi_url):
        self.__base_url = re.sub('(.*)://([^/]+).*', '\\1://\\2/nifi-api/', nifi_url)
        self.__current_user = self.get_current_user()
        self.__client_id = self.get_client_id()

    @property
    def base_url(self):
        return self.__base_url

    @property
    def current_user(self):
        return self.__current_user
    
    @property
    def client_id(self):
        return self.__client_id

    def get_current_user(self):
        end_point = "{}flow/current-user".format(self.__base_url)
        response = requests.get(end_point)
        if (response.status_code != 200):
            raise Exception("Unable to get current user from {}.".format(end_point))
        return response.json()

    def get_client_id(self):
        end_point = "{}flow/client-id".format(self.__base_url)
        response = requests.get(end_point)
        if (response.status_code != 200):
            raise Exception("Unable to get client id from {}.".format(end_point))
        return response.text

    def get_search(self, query):
        params = {'q': query}
        end_point = "{}flow/search-results".format(self.__base_url)
        response = requests.get(end_point, params=params)
        if (response.status_code != 200):
            print(response)
            raise Exception("Unable to perform search for {} from {}.".format(query, end_point))
        return response.json()

    def get_process_group(self, group_id):
        end_point = "{}flow/process-groups/{}".format(self.__base_url, group_id)
        response = requests.get(end_point)
        if (response.status_code != 200):
            raise Exception("Unable to get process group from {}.".format(end_point))
        return response.json()
        
    def get_processor(self, processor_id):
        end_point = "{}processors/{}".format(self.__base_url, processor_id)
        response = requests.get(end_point)
        if (response.status_code != 200):
            raise Exception("Unable to get processor from {}.".format(end_point))
        return response.json()
        




class VancunNiFiShell(cmd.Cmd):

    def __init__(self, nifi_url):
        super().__init__()
        self.prompt = 'nifi> '
        self.nifi_url = nifi_url

    def preloop(self):
        super().preloop()
        nifi = VancunNiFiClient(self.nifi_url)
        self.nifi = nifi
        print("Connected to '{nifi}' as '{user}'. Client ID: '{id}'.".format(nifi=nifi.base_url, id=nifi.client_id, user=nifi.current_user['identity']))
        print("Type '?' or 'help' for help, 'bye' to exit.")


    def var_dumps(self, var, options={}):
        var = self.apply_path(options.get('path',''),var,options.get('root',None))
        if (type(var) is dict and options.get('dump','') == 'keys'):
            return ', '.join(var.keys())
        if (type(var) is list or type(var) is dict):
            json_options = {k[5:]:(int(options[k]) if options[k].isnumeric() else options[k]) for k in options if k[:5] == 'json-'}
            return json.dumps(var, **json_options)
        else:
            return var

    def var_print(self, var, options={}):
        print(self.var_dumps(var, options))

    def handle_result(self, var, options={}):
        str = self.var_dumps(var, options)
        if (options.get('file', False)):
            with open(options['file'], 'w') as f:
                f.write(str)
        if ('noprint' not in options):
            print(str)

    def parse_arg(self, arg, defaults={}, arg_key='') :
        result = {k:defaults[k] for k in defaults}
        for option_string in arg.split(' '):
            *key,value = option_string.split('=',2)
            if (key):
                str_key = key[0]
            else:
                if (arg_key in result):
                    str_key = value
                else:
                    str_key = arg_key
            result[str_key] = value
        return result

    def apply_path(self, path, var, root=None):
        result = var
        if (root):
            result = var[root]
        for node_key in path.split('.'):
            if (node_key == ''):
                break
            elif (node_key == '#'):
                if (type(result) is list):
                    result = len(result)
                elif (type(result) is dict):
                    result = len(result.keys())
                break
            result = result[int(node_key) if node_key.isnumeric() else node_key]
        return result

    def info_user(self):
        return self.nifi.current_user

    def info_client_id(self):
        return self.nifi.client_id

    def info_base_url(self):
        return self.nifi.base_url

    def do_info(self, arg):
        """Get NiFi information.
           Syntax: info {user|client_id|base_url}"""
        
        try:
            options = self.parse_arg(arg, arg_key='what')
            method = "info_" + options['what']
            method_ref = getattr(self, method, None)
            if (method_ref is None):
                print("'{}' is not a valid attribute.".format(arg))
            else:
                self.handle_result(method_ref(), options)
        except Exception as ex:
            print("ERROR: {}".format(ex))

    def do_get_pg(self, arg):
        """Get process group

           Syntax: get_pg [id=]<process-group-id>
           Defaults: root=processGroupFlow
        """
        try:
            options = self.parse_arg(arg, arg_key='id')
            options['root'] = options.get('root', 'processGroupFlow')
            group_id = options.get('id')
            pg = self.nifi.get_process_group(group_id)
            self.handle_result(pg, options)
            # self.handle_result(self.apply_path(path, pg, "processGroupFlow"))
        except Exception as ex:
            print("ERROR: {}".format(ex))

    def do_get_p(self, arg):
        """Get processor
        
           Syntax: get_p [id=]<processor-id>
           Defaults: root=processGroupFlow
        """
        try:
            options = self.parse_arg(arg, arg_key='id')
            p = self.nifi.get_processor(options['id'])
            self.handle_result(p, options)
        except Exception as ex:
            print("ERROR: {}".format(ex))


    def do_search(self, arg):
        """Performs search against this NiFi, using the query.
        
           Syntax: search [query=]<search-query>
           Defaults: root=searchResultsDTO"""

        try:
            options = self.parse_arg(arg, arg_key='query')
            options['query'] = options.get('query', '')
            options['root'] = options.get('root', 'searchResultsDTO')
            self.handle_result(self.nifi.get_search(options['query']), options)
        except Exception as ex:
            print("ERROR: {}".format(ex))

    def do_options(self, arg):
        """Global options:
           json-<option> (see json.dumps)
              skipkeys=False, ensure_ascii=True, check_circular=True, 
              allow_nan=True, cls=None, indent=None, separators=None, 
              default=None, sort_keys=False
           file=<filename>  - save to file
           noprint - do not print
           root=<path> - dump from json path
           dump={json|keys}
              default=json
        """

    def do_bye(self, arg):
        """End interactive NiFi session."""
        return True


@click.group()
def cli():
    pass

@cli.command()
@click.argument('nifi_url', default='http://localhost:8080')
def shell(nifi_url):
    """Interactive nifi shell"""

    nifi = VancunNiFiShell(nifi_url)
    nifi.cmdloop()

if (__name__ == "__main__"):
    cli()
