#!/usr/bin/python3

class Square:
    """A class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): The size of the new square
            position (0, 0): The position of the new square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/Set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/Set the current size of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple(0, 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current Area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print(" ") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
