#!/usr/bin/python3

"""A function that replaces all occurrences of an
    element by another in a new list."""


def search_replace(my_list, search, replace):
    return ([replace if x is search else x for x in my_list])
