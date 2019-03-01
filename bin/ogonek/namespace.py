import doctest


class Namespace(dict):
    """Dictionary-like (key,value) collection which
    keys as object properties.

    # Create Namespace Objects

    Create an empty Namespace object:
    >>> Namespace()
    Namespace({})

    Create a Namespace object from a dictionary:
    >>> Namespace({'some': 'thing'})
    Namespace({'some': 'thing'})

    # Operations with elements
    >>> ns = Namespace({'a':15, 'b':'John'})

    Elements in the collection can be accessed as object attributes.
    >>> ns.a
    15

    Elements could also be accessed as dictionary elements.
    >>> ns['b']
    'John'

    Accessing non-existent element as attribute results in an error.
    >>> ns.c
    Traceback (most recent call last):
    ...
    AttributeError: 'Namespace' object has no attribute 'c'

    Attributes could be set.
    >>> ns.d = 'Ivan'
    >>> ns.d
    'Ivan'

    Attribute could be removed.
    >>> del(ns.d)
    >>> 'd' in ns
    False

    Remove attribute the dictionary way.
    >>> ns1 = Namespace({'d':'John'})
    >>> del(ns['d'])
    >>> 'd' in ns
    False
    """

    def __init__(self, mappings=[]):
        """Initialize the object.

        Creating Namespace object without mappings creates empty
        Namespace.
        >>> Namespace()
        Namespace({})

        If dictionary is passed to the constructor, elements are
        added to the Namespace.
        >>> Namespace({'a':'b'})
        Namespace({'a': 'b'})

        If a list of key-value pairs is passed to the constructor,
        elements are added to the Namespace.
        >>> Namespace([('a', 15)])
        Namespace({'a': 15})
        """
        super().__init__(mappings)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (type(self).__name__, name))

    def __dir__(self):
        return dir({}) + list(self.keys())

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, super().__repr__())


if __name__ == "__main__":
    doctest.testmod()
