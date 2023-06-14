#!/usr/bin/python3
"""
Defines an obj student
and  a funtion that serializes a dictionary
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the object to a JSON serializable dictionary.
        If `attrs` is None,
        returns a dictionary representation of the
        entire object's attributes.
        Otherwise, returns a dictionary
        representation of only the specified `attrs`.
        :param attrs: A list of attribute names to include in the dictionary.
        Defaults to None.
        :type attrs: Optional[List[str]]
        :return: A dictionary representation of the object.
        :rtype: Dict[str, Any]
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
