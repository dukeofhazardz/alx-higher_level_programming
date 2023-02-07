#!/usr/bin/python3

"""A class that defines BaseGeometry"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """Returns the area of the shape"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates the value"""

        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class that defines a Rectangle"""

    def __init__(self, width, height):
        """Initializes the Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """Returns the Rectangle's description"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """A class that defines a Square"""

    def __init__(self, size):
        """Initializes the Square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
