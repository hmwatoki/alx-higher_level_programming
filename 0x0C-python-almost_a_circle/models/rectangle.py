#!/usr/bin/python3
"""Creats a subclass rectangle"""


from base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle class
        with width, height, x, y, and id attributes.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter methods
    def get_width(self):
        """
        Returns the width attribute of the Rectangle object.
        """
        return self.__width

    def get_height(self):
        """
        Returns the height attribute of the Rectangle object.
        """
        return self.__height

    def get_x(self):
        """
        Returns the x attribute of the Rectangle object.
        """
        return self.__x

    def get_y(self):
        """
        Returns the y attribute of the Rectangle object.
        """
        return self.__y

    # Setter methods
    def set_width(self, value):
        """
        Sets the width attribute of the Rectangle object to the given value.
        """
        self.__width = value

    def set_height(self, value):
        """
        Sets the height attribute of the Rectangle object to the given value.
        """
        self.__height = value

    def set_x(self, value):
        """
        Sets the x attribute of the Rectangle object to the given value.
        """
        self.__x = value

    def set_y(self, value):
        """
        Sets the y attribute of the Rectangle object to the given value.
        """
        self.__y = value
