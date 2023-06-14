#!/usr/bin/python3
"""Converts obj to string"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object into a JSON string representation.

    Args:
        my_obj (Any): The Python object to be converted.

    Returns:
        str: The JSON string representation of the given object.
    """
    json_str = json.dumps(my_obj)
    return json_str
