#!/usr/bin/python3
"""Defines a class-checking function."""


class MyList(list):
    """A class that inherits from 'list'"""

    def print_sorted(self):
        """A method that prints the list,
        but sorted (ascending sort)"""

        print(sorted(self))
