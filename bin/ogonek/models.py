

class ProcessFlow:
    """Model class representing process flow.
    """

    def __init__(self, name, parameters):
        """Initialize new object.

        >>> ProcessFlow('my_flow', {'age':16})
        {'name': 'my_flow', 'parameters': {'age': 16}}
        """
        self._name = name
        self._params = dict(parameters if parameters else {})
        self._activity_list = []
        self._activities = {}

    @property
    def name(self):
        """Get the flow name.

        >>> ProcessFlow('my_flow', {'age':16}).name
        'my_flow'
        """
        return self._name

    @property
    def parameters(self):
        """Get the flow parameters.

        >>> ProcessFlow('my_flow', {'age':16}).parameters
        {'age': 16}
        >>> ProcessFlow('my_flow', None).parameters
        {}
        """
        return self._params

    @property
    def num_activities(self):
        """Get the number of activities.

        >>> a = FlowActivity('activity_1', 'read_file', None, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f.add_activity(a).num_activities
        1
        """
        return len(self._activities)

    def add_activity(self, activity):
        """Get activity by name or index.

        >>> a = FlowActivity('activity_1', 'read_file', None, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f.add_activity(a).get_activity(0)
        {'name': 'activity_1', 'type': 'read_file'}
        >>> f.add_activity(a)
        Traceback (most recent call last):
        ...
        KeyError: "Activity 'activity_1' already exists."
        """
        if activity.name in self._activities:
            raise KeyError(
                "Activity '{}' already exists.".format(activity.name))
        self._activities[activity.name] = {
            'index': len(self._activity_list),
            'activity': activity
        }
        self._activity_list.append(activity.name)
        return self

    def has_activity(self, name_or_index):
        """Check if activity exists in flow.

        >>> a = FlowActivity('activity_1', 'read_file', None, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f.add_activity(a).has_activity('activity_1')
        True
        >>> f.has_activity('activity_122')
        False
        >>> f.has_activity(0)
        True
        >>> f.has_activity(1)
        False
        """
        if type(name_or_index) is int:
            return name_or_index in (0, len(self._activity_list)-1)
        else:
            return name_or_index in self._activities

    def get_activity(self, name_or_index):
        """Get activity by name or index.

        >>> a = FlowActivity('activity_1', 'read_file', None, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f.add_activity(a).get_activity(0)
        {'name': 'activity_1', 'type': 'read_file'}
        >>> f.get_activity('activity_1')
        {'name': 'activity_1', 'type': 'read_file'}
        >>> f.get_activity(5555)
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        >>> f.get_activity('missing_activity')
        Traceback (most recent call last):
        ...
        KeyError: 'missing_activity'
        """
        name = self._activity_list[name_or_index] if type(
            name_or_index) is int else name_or_index
        return self._activities[name]['activity']

    def get_activity_index(self, activity):
        """Get activity index by name or activity.
        >>> a = FlowActivity('activity_1', 'read_file', None, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f.add_activity(a).get_activity_index('activity_1')
        0
        >>> f.get_activity_index(a)
        0
        """
        name = activity.name if type(activity) is FlowActivity else activity
        return self._activities[name]['index']

    def get_next_activity_when_ok(self, activity):
        """Find next activity when specified activity finishes OK.

        Let's create a new flow
        >>> a = FlowActivity('activity_1', 'read_file', None, 'send_email', 'abort')
        >>> b = FlowActivity('send_email', 'mailer', None, None, None)
        >>> c = FlowActivity('last_step', 'dummy', None, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f = f.add_activity(a).add_activity(b).add_activity(c)

        Activity could be FlowActivity
        >>> f.get_next_activity_when_ok(a)
        {'name': 'send_email', 'type': 'mailer'}

        Activity could be activity name
        >>> f.get_next_activity_when_ok('activity_1')
        {'name': 'send_email', 'type': 'mailer'}

        Activity could be activity index
        >>> f.get_next_activity_when_ok('activity_1')
        {'name': 'send_email', 'type': 'mailer'}

        If activity has no when_ok, next in the list is returned.
        >>> f.get_next_activity_when_ok('send_email')
        {'name': 'last_step', 'type': 'dummy'}

        If activity has no when_ok and is last activity, None is returned.
        >>> f.get_next_activity_when_ok('last_step') is None
        True
        """
        if type(activity) is not FlowActivity:
            activity = self.get_activity(activity)
        next = activity.when_ok
        if type(next) is int:
            return self.get_activity(next)
        elif next is not None:
            return self.get_activity(next)
        next = self.get_activity_index(activity) + 1
        if self.has_activity(next):
            return self.get_activity(next)
        return None

    def as_dict(self):
        """Get flow serialized as dictionary.
        >>> a = FlowActivity('activity_1', 'read_file', {'name':'users.json'}, None, None)
        >>> f = ProcessFlow('my_flow',{})
        >>> f.add_activity(a).as_dict()
        {'name': 'my_flow', 'activities': [{'name': 'activity_1', 'type': 'read_file', 'parameters': {'name': 'users.json'}}]}
        """
        d = {
            'name': self._name
        }
        if self._params:
            d['parameters'] = self._params
        if self._activity_list:
            d['activities'] = [self._activities[name]['activity']
                               for name in self._activity_list]

        return d

    def __repr__(self):
        return self.as_dict().__repr__()

    @classmethod
    def _create_activity(cls, activity_definition):
        args = {}
        args['name'] = activity_definition['name']
        args['activity_type'] = activity_definition['type']
        args['parameters'] = activity_definition.get('parameters', {})
        args['when_ok'] = activity_definition.get('when_ok', None)
        args['when_error'] = activity_definition.get('when_error', None)
        activity = FlowActivity(**args)
        return activity

    @classmethod
    def from_dict(cls, definition):
        """
        >>> ProcessFlow.from_dict({
        ...    'name': 'my_flow',
        ...    'parameters': {'day':'Monday'},
        ...    'activities': [{'name':'activity_1', 'type':'read_file', 'parameters': {'name':'users.json'}, 'when_ok':'send_email', 'when_error':'abort'}]
        ... })
        {'name': 'my_flow', 'parameters': {'day': 'Monday'}, 'activities': [{'name': 'activity_1', 'type': 'read_file', 'parameters': {'name': 'users.json'}, 'when_ok': 'send_email', 'when_error': 'abort'}]}

        Many attributes are optional.
        >>> ProcessFlow.from_dict({'name': 'my_flow'})
        {'name': 'my_flow'}
        """
        flow = cls(definition.get('name', 'Unnamed Flow'),
                   definition.get('parameters', {}))
        for activity_definition in definition.get('activities', []):
            activity = cls._create_activity(activity_definition)
            flow.add_activity(activity)
        return flow


class FlowActivity:
    """Model class, representing flow activity.
    """

    def __init__(self, name, activity_type, parameters, when_ok, when_error):
        """Initialize new activity.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error')
        {'name': 'activity_1', 'type': 'read_file', 'parameters': {'filename': 'users.json'}, 'when_ok': 'send_email', 'when_error': 'fail_with_error'}
        """
        self._name = name
        self._type = activity_type
        self._params = dict(parameters if parameters else {})
        self._when_ok = when_ok
        self._when_error = when_error

    @property
    def name(self):
        """Get flow name.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error').name
        'activity_1'
        """
        return self._name

    @property
    def activity_type(self):
        """Get activity type.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error').activity_type
        'read_file'
        """
        return self._type

    @property
    def parameters(self):
        """Get activity parameters.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error').parameters
        {'filename': 'users.json'}
        """
        return self._params

    @property
    def when_ok(self):
        """Get activity to be executed next on successfull activity execution.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error').when_ok
        'send_email'
        """
        return self._when_ok

    @property
    def when_error(self):
        """Get activity to be executed next on activity execution error.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error').when_error
        'fail_with_error'
        """
        return self._when_error

    @property
    def as_dict(self):
        """Get activity as dictionary. Empty parameters, when_ok and when_error are not included.

        >>> FlowActivity('activity_1', 'read_file', {'filename': 'users.json'}, 'send_email', 'fail_with_error').as_dict
        {'name': 'activity_1', 'type': 'read_file', 'parameters': {'filename': 'users.json'}, 'when_ok': 'send_email', 'when_error': 'fail_with_error'}

        Empty parameters are not included.
        >>> FlowActivity('activity_1', 'read_file', {}, 'send_email', 'fail_with_error').as_dict
        {'name': 'activity_1', 'type': 'read_file', 'when_ok': 'send_email', 'when_error': 'fail_with_error'}

        >>> FlowActivity('activity_1', 'read_file', None, 'send_email', 'fail_with_error').as_dict
        {'name': 'activity_1', 'type': 'read_file', 'when_ok': 'send_email', 'when_error': 'fail_with_error'}

        Empty when_ok is not included.
        >>> FlowActivity('activity_1', 'read_file', None, None, 'fail_with_error').as_dict
        {'name': 'activity_1', 'type': 'read_file', 'when_error': 'fail_with_error'}

        Empty when_error is not included.
        >>> FlowActivity('activity_1', 'read_file', None, 'send_email', None).as_dict
        {'name': 'activity_1', 'type': 'read_file', 'when_ok': 'send_email'}
        """
        d = {
            'name': self._name,
            'type': self._type
        }
        if self._params:
            d['parameters'] = dict(self._params)
        if self._when_ok is not None:
            d['when_ok'] = self._when_ok
        if self._when_error is not None:
            d['when_error'] = self._when_error
        return d

    def __repr__(self):
        return "{}".format(self.as_dict)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
