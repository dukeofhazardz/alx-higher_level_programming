#!/usr/bin/python3
"""Defines a class-checking function."""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the specified
    class; Otherwise False."""

    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
