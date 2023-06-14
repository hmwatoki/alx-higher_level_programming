#!/usr/bin/python3
"""Defines load from json function"""
import json


def load_from_json_file(filename: str) -> any:
    """
    Loads data from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        The JSON data loaded from the specified file.
    """
    with open(filename, mode="r") as file:
        return json.load(file)
