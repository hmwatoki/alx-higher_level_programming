#!/usr/bin/python3
"""Creats a subclass rectangle"""


from models.base import Base


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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    def set_height(self, value):
        """
        Sets the height attribute of the Rectangle object to the given value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    def set_x(self, value):
        """
        Sets the x attribute of the Rectangle object to the given value.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    def set_y(self, value):
        """
        Sets the y attribute of the Rectangle object to the given value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def display(self):
        """Displays rectangle"""
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """Overrides default string representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id,
            self.get_x(),
            self.get_y(),
            self.get_width(),
            self.get_height()
        )
