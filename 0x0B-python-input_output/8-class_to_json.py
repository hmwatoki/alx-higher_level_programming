#!/usr/bin/python3
"""Defines a Py class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of python data structure."""
    return obj.__dict__
