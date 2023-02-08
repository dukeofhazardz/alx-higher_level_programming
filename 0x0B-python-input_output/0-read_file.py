#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Opens and reads a text file to stdout:"""
    with open(filename, "r") as f:
        print(f.read(), end="")
