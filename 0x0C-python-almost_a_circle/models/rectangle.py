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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter methods
    @property
    def width(self):
        """
        Returns the width attribute of the Rectangle object.
        """
        return self.__width

    @property
    def height(self):
        """
        Returns the height attribute of the Rectangle object.
        """
        return self.__height

    @property
    def x(self):
        """
       Returns the x attribute of the Rectangle object.
        """
        return self.__x

    @property
    def y(self):
        """
         Returns the y attribute of the Rectangle object.
         """
        return self.__y

    # Setter methods
    @width.setter
    def width(self, value):
        """Sets the width attribute of the Rectangle object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute of the Rectangle object"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute of the Rectangle object"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute of the Rectangle object"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a string representation of the Rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def __str__(self):
        """Overrides default string representation"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
