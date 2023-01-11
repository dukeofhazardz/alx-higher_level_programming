#!/usr/bin/python3

"""A function that returns a set of common elements in two sets."""


def common_elements(set_1, set_2):
    for i in set_1:
        for j in set_2:
            if i is j:
                set_3 = i
    return set_3
