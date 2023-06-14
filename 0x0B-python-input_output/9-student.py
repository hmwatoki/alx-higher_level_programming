#!/usr/bin/python3
"""Initializes an obj an returns its dictionary"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initializes a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the object's
        """
        return self.__dict__
