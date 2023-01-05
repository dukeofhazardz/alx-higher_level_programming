#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("0 arguements.", end="\n")

    elif length == 1:
        print("1 arguement:", end="\n")

    else:
        print("{} arguements:".format(length, end="\n"))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]), end="\n")
