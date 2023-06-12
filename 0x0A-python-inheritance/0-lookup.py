#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.

    :param obj: an object to inspect
    :type obj: Any
    :return: a list of attributes and methods
    :rtype: List[str]
    """
    attributes = []
    methods = []

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

    return attributes + methods
