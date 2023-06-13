#!/usr/bin/python3
"""adds a new attribute ony if possible"""


def add_attribute(obj, attr, value):
    """function that adds new attribute"""
    if('__slots__' in dir(obj) or '__dict__' not in dir(obj) or
       hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
