#!/usr/bin/python3
"""A class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle classs"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets/Sets the Width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets the Height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets/Sets the 'x' attribute of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets/Sets the 'y' attribute of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#'"""
        if (self.__y):
            for m in range(self.__y):
                print("")
        for i in range(self.__height):
            if (self.__x):
                print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Updates the values of the 'Rectangle' class"""
        if (args):
            length = len(args)
            if (length == 1):
                self.id = args[0]
            elif (length == 2):
                self.id = args[0]
                self.width = args[1]
            elif (length == 3):
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif (length == 4):
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif (length == 5):
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        elif (kwargs):
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
            for key, value in kwargs.items():
                if key == "height":
                    self.height = value
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
            for key, value in kwargs.items():
                if key == "x":
                    self.x = value
            for key, value in kwargs.items():
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the 'Rectangle' class"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns the decription of the Rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}\
            ".format(self.id, self.x, self.y, self.width, self.height)
