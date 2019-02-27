
import json

__all__ = ['DataPipelineFactory']


class DataPipelineFactory:

    @staticmethod
    def _validate_descriptor(descriptor):
        if 'name' not in descriptor:
            raise Exception("'name' not found in definition.")

        if 'parameters' not in descriptor:
            raise Exception("'parameters' not found in definition.")
        if not isinstance(descriptor['parameters'], dict):
            raise Exception("'parameters' should be dictionary.")

        if 'pipeline' not in descriptor:
            raise Exception("'pipeline' not found in definition.")
        pipeline = descriptor['pipeline']
        if not isinstance(pipeline, dict):
            raise Exception("'pipeline' should be dictionary.")

        if 'steps' not in pipeline:
            raise Exception("'steps' not found in definition.")
        steps = pipeline['steps']
        if not isinstance(steps, list):
            raise Exception("'steps' for pipeline should be a list.")

        for step_num, step in enumerate(steps):
            if not isinstance(step, dict):
                raise Exception('Step #{} should be dictionary. Found {}.'.format(
                    step_num, type(step).__name__))
            if 'name' not in step:
                raise Exception("Step #{} should have 'name'".format(step_num))
            if 'type' not in step:
                raise Exception("Step #{} should have 'type'".format(step_num))

            if 'properties' in step:
                properties = step['properties']
                if not isinstance(properties, dict):
                    raise Exception('Properties for step #{} should be a dictionary. Found {}.'.format(
                        step_num, type(properties).__name__))

        return descriptor

    @classmethod
    def from_dict_descriptor(cls, descriptor):
        cls._validate_descriptor(descriptor)
        pipeline = DataPipeline(descriptor['name'])
        if 'description' in descriptor:
            pipeline.description = descriptor['description']
        if 'parameters' in descriptor:
            pipeline._params = dict(descriptor['parameters'])
        if 'variables' in descriptor:
            pipeline._vars = dict(descriptor['variables'])
        pipeline_descriptor = descriptor['pipeline']
        step_descriptors = pipeline_descriptor['steps']
        for step in step_descriptors:
            pipeline._steps.append(DataPipelineStep.from_descriptor(step))
        return pipeline

    @classmethod
    def from_json_file_descriptor(cls, fp):
        return cls.from_dict_descriptor(json.load(fp))


class DataPipelineStep:
    def __init__(self, name, step_type):
        self._name = name
        self._type = step_type
        self._description = None
        self._vars = {}

    @property
    def as_dict(self):
        d = {
            'name': self._name,
            'type': self._type
        }
        if (self._vars):
            d['variables'] = self._vars
        if (self._description):
            d['description'] = self._description
        return d

    @property
    def step_type(self):
        return self._type

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def variables(self):
        return self._vars

    @classmethod
    def from_descriptor(cls, desc):
        step = cls(desc['name'], desc['type'])
        if 'variables' in desc:
            step._vars = dict(desc['variables'])
        if 'description' in desc:
            step._description = desc['description']
        return step


class DataPipeline:
    def __init__(self, name):
        self._name = name
        self._description = None
        self._steps = []
        self._params = {}
        self._vars = {}

    def __repr__(self):
        return (self.as_json)

    @property
    def variables(self):
        return self._vars

    @property
    def steps(self):
        return self._steps

    @property
    def name(self):
        return self._name

    @property
    def parameters(self):
        return self._params

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def as_dict(self):
        descriptor = {
            'name': self._name,
            'parameters': dict(self._params),
            'variables': dict(self._vars),
            'steps': list()
        }
        if self._description is not None:
            descriptor['description'] = self._description
        for step in self._steps:
            descriptor['steps'].append(step.as_dict)
        return descriptor

    @property
    def as_json(self):
        return json.dumps(self.as_dict)

    @description.setter
    def description(self, description):
        self._description = description
