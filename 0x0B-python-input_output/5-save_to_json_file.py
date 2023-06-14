#!/usr/bin/python3
"""Defines save to json function"""
import json



def save_to_json_file(my_obj, filename):
    """
    Saves object to a json file specified
    args: object, filename
    Returns: none
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
