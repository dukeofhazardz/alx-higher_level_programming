#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("{} arguments.".format(length), end="\n")

    elif length == 1:
        print("{} argument:".format(length), end="\n")

    else:
        print("{} arguments:".format(length), end="\n")

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]), end="\n")
