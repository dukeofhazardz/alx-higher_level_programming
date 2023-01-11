#!/bin/python3

"""A function that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        if(a_dictionary.get(key)):
            del a_dictionary[key]
    return a_dictionary
