#!/usr/bin/python3
"""A class 'Square' that inherits from 'Rectangle'"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets/Sets the size attribute of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the 'Square' class"""
        if (args):
            length = len(args)
            if (length == 1):
                self.id = args[0]
            elif (length == 2):
                self.id = args[0]
                self.size = args[1]
            elif (length == 3):
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif (length == 4):
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        elif (kwargs):
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
            for key, value in kwargs.items():
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the 'Square'"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns the description of the 'Square' class"""
        return "[Square] ({}) {}/{} - {}\
                ".format(self.id, self.x, self.y, self.width)
