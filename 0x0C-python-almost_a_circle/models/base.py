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
            the `id` attribute. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        The filename is <Class name>.json and overwrites any existing file.

        If list_objs is None, saves an empty list.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            Nothing. Writes to a file instead.

        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, mode='w', encoding='utf-8') as f:
                f.write("[]")
                return

        list_dict = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            list_dict.append(obj_dict)

        json_str = cls.to_json_string(list_dict)

        # Write JSON string to file

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(json_str)
