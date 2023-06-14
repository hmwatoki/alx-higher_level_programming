#!/usr/bin/python3
"""converts json string to an object"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        Any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
