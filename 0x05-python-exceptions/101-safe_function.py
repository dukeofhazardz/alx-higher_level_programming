#!/usr/bin/python3
import sys

"""A function that executes a function safely."""


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except (ValueError, ZeroDivisionError, TypeError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
