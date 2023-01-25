#!/usr/bin/python3

class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): The size of the new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current Area of a Square"""
        return (self.__size * self.__size)
