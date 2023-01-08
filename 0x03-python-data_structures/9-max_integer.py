#!/usr/bin/python3

"""A function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = my_list[0]

    for i in range(0, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max
