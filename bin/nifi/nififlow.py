
__all__ = [ 'NiFiProcessGroup' ]

"""Contains defintions for classes which wrap flow object results from NiFi REST calls."""

class NiFiPort:
    def __init__(self, nifi_def):
        self._nifi_def = nifi_def


    @property
    def id(self):
        return self._nifi_def['component']['id']

    @property
    def name(self):
        return self._nifi_def['component']['name']

    @property
    def group_id(self):
        return self._nifi_def['component']['parentGroupId']


class NiFiInputPort(NiFiPort):
    pass

class NiFiOutputPort(NiFiPort):
    pass

class NiFiProcessGroup:
    def __init__(self, nifi_def):
        self._nifi_def = nifi_def

    @property
    def id(self):
        return self._nifi_def['component']['id']

    @property
    def name(self):
        return self._nifi_def['component']['name']



class NiFiProcessGroupFlow:
    _inports = None
    _outports = None

    def __init__(self, nifi_def):
        self._nifi_def = nifi_def

    @property
    def id(self):
        return self._nifi_def['processGroupFlow']['id']

    @property
    def name(self):
        return self._nifi_def['processGroupFlow']['breadcrumb']['breadcrumb']['name']

    @property
    def inports(self):
        if self._inports is None:
            inports = []
            for p in self._nifi_def['processGroupFlow']['flow']['inputPorts']:
                inports.append(NiFiInputPort(p))
            self._inports = inports
        return self._inports

    @property
    def outports(self):
        if self._outports is None:
            outports = []
            for p in self._nifi_def['processGroupFlow']['flow']['outputPorts']:
                outports.append(NiFiInputPort(p))
            self._outports = outports
        return self._outports
            
    def get_inport(self, name):
        for p in self.inports:
            if p.name == name:
                return p
        return None

    def get_outport(self, name):
        for p in self.outports:
            if p.name == name:
                return p
        return None
