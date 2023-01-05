#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    length = len(sys.argv) - 1

    if length == 0:
        print("0 arguements.")

    elif length == 1:
        print("1 arguement:")

    else:
        print("{} arguements:".format(length))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
