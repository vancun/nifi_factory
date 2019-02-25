import requests
import re
import json

class NiFiClient:
    """Implement NiFi REST Client
    """
    __root_id = None
    
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

    @property
    def root_id(self):
        if (not self.__root_id):
            root_pg = self.get_process_group('root')
            self.__root_id = root_pg['processGroupFlow']['id']
        return self.__root_id

    def get_templates(self):
        end_point = "{}flow/templates".format(self.__base_url)
        response = requests.get(end_point)
        if (response.status_code != 200):
            raise Exception("Unable to get current user from {}.".format(end_point))
        return response.json()


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
            raise Exception("Unable to get process group flow from {}.".format(end_point))
        return response.json()
        
    def get_pg(self, group_id):
        end_point = "{}process-groups/{}".format(self.__base_url, group_id)
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

    def delete_process_group(self, group_id, version):
        end_point = "{}process-groups/{}".format(self.__base_url, group_id)
        params = { 
            'version': version,
            'clientId': self.client_id, 
            'disconnectedNodeAcknowledged': False }
        response = requests.delete(end_point, params=params)
        if (response.status_code != 200):
            print(response)
            raise Exception("Unable to delete process group {}.".format(group_id))
        return response.json()
    
    def create_process_group(self, name, parent_id, pos_x=None, pos_y=None):
        params = {
            'revision': {'clientId': self.client_id, 'version': 0},
            'disconnectedNodeAcknowledged': False,
            'component': {
                'name': name,
                'position': {}
            }
        }
        if (pos_x is not None):
            params['component']['position']['x'] = pos_x
        if (pos_y is not None):
            params['component']['position']['y'] = pos_y
        end_point = "{}process-groups/{}/process-groups".format(self.__base_url, parent_id)
        response = requests.post(end_point, json=params)
        if (response.status_code != 201):
            print(response)
            raise Exception("Unable to create process group {}.".format(name))
        return response.json()

    def configure_pg(self, id, name=None, comments=None):
        pg = self.get_pg(id)
        params = {
            "revision": {
                "clientId": self.__client_id,
                "version": 0
            },
            "disconnectedNodeAcknowledged": False,
            "component": {
                "id": id
            }
        }
        if name:
            params['component']['name'] = name
        if comments:
            params['component']['comments'] = comments
        end_point = "{}process-groups/{}".format(self.__base_url, id)
        response = requests.put(end_point, json=params)
        if (response.status_code != 200):
            print(response)
            raise Exception("Unable to configure process group {}.".format(id))
        return response.json()


    def add_connection(self, group_id, info):
        """
        """
        end_point = "{}process-groups/{}/connections".format(self.__base_url, group_id)
        params = {
            "revision": {
                "clientId": self.__client_id,
                "version": 0
            },
            "disconnectedNodeAcknowledged": False,
            "component": info
        }
        response = requests.post(end_point, json=params)
        if (response.status_code != 201):
            print(response)
            raise Exception("Unable to add connection {}.".format(template_id))
        return response.json()



    def instantiate_template(self, group_id, template_id, origin_x=0, origin_y=0):
        end_point = "{}process-groups/{}/template-instance".format(self.__base_url, group_id)
        params = {
            'templateId': template_id,
            'originX': origin_x,
            'originY': origin_y,
            'disconnectedNodeAcknowledged': False
        }
        response = requests.post(end_point, json=params)
        if (response.status_code != 201):
            print(response)
            raise Exception("Unable to instantiate template {}.".format(template_id))
        return response.json()

    def get_pg_vars(self, id):
        end_point = "{base}process-groups/{id}/variable-registry".format(base=self.__base_url, id=id)
        response = requests.get(end_point)
        if (response.status_code != 200):
            print(response)
            raise Exception("Unable to get variables for {}.".format(id))
        return response.json()

    def update_pg_vars(self, id, vars):
        end_point = "{base}process-groups/{id}/variable-registry".format(base=self.__base_url, id=id)
        pg = self.get_pg(id)

        vr = []
        for n in vars:
            vr.append({
                "variable": {
                    "name": n,
                    "value": vars[n]
                }
            })

        params = {
            'processGroupRevision': {
                "clientId": self.client_id,
                "version": pg['revision']['version']
            },
            "disconnectedNodeAcknowledged": False,
            "variableRegistry": {
                "processGroupId": id,
                "variables": vr
            }
        }
        response = requests.put(end_point, json=params)
        if (response.status_code != 200):
            print(response)
            raise Exception("Unable to update vars for {}.".format(id))
        return response.json()



