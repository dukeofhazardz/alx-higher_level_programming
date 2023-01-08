#!/usr/bin/python3

"""A function that deletes the item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    del my_list[idx]
    new_list = []

    for i in my_list:
        new_list.append(i)
    return new_list
