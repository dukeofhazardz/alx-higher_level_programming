#!/usr/bin/python3

#A program that prints the number of and the list of its arguments.

if __name__ == "__main__":

    import sys

    length = len(sys.argv) - 1

    if length == 1:
        print("{} arguement:".format(length), end="\n")

    elif length == 0:
        print("0 arguement.", end="\n")

    else:
        print("{} arguements:".format(length, end="\n"))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]), end="\n")
