#!/usr/bin/python3
import sys

"""A function that executes a function safely."""


def safe_function(fct, *args):
    a, b = args
    try:
        result = fct(a, b)
        return (result)
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        result = None
        print("Exception: {}".format(sys.exc_info()[1]))
        return (result)
