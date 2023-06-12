#!/usr/bin/python3
"""Defines a function to return a list of attributes"""


def lookup(obj):
    """Returns a list of attributes the given object."""
    return dir(obj)
