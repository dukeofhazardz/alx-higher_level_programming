#!/usr/bin/python3
"""Invert int operators == and !=."""


class MyInt(int):
    """A class the defines MyInt"""

    def __eq__(self, value):
        """A method that defines the equal-to operator"""
        return (self.real != value)

    def __ne__(self, value):
        """A method that defines the not-equal-to operator"""
        return (self.real == value)
