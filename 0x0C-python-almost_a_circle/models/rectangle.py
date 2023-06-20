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

    # validator
    def validator(self, name, value):
        """validates the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name is 'width' or name is 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name is 'x' or name is 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    # Getter methods
    def width(self):
        """
        Returns the width attribute of the Rectangle object.
        """
        return self.__width

    def height(self):
        """
        Returns the height attribute of the Rectangle object.
        """
        return self.__height

    def x(self):
        """
        Returns the x attribute of the Rectangle object.
        """
        return self.__x

    def y(self):
        """
        Returns the y attribute of the Rectangle object.
        """
        return self.__y

    # Setter methods
    def width(self, value):
        """
        Sets the width attribute of the Rectangle object to the given value.
        """
        self.validator("width", value)
        self.__width = value

    def height(self, value):
        """sets height"""
        self.validator("height", value)
        self.__height = value

    def x(self, value):
        """
        Sets the x attribute of the Rectangle object to the given value.
        """
        self.validator("x", value)
        self.__x = value

    def y(self, value):
        """
        Sets the y attribute of the Rectangle object to the given value.
        """
        self.validator("y", value)
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
