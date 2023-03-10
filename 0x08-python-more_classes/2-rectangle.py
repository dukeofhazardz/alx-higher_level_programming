#!/usr/bin/python3

"""Defines a Rectangle Class"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/Sets the current width of the Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets the current height of the Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the Area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the Perimeter of the Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width + self.__height) * 2)
