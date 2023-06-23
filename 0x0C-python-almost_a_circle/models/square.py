#!/usr/bin/python3
"""Defines a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square class with size, x, y, and id attr.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns the size attribute of the Square instance.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size attribute of the Square instance.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )
