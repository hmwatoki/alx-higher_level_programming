#!/usr/bin/python3
"""Defines a base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the `Base` class by assigning the attributes
        Args:
            id (int, optional): An integer value representing
            the `id` attribute.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):

        if list_dictionaries is not None or len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
