#!/usr/bin/python3

if __name__ == "__main__":

    """A program that prints the result of the addition of all arguments"""

    import sys

    sum = 0
    for numbers in range(1, len(sys.argv)):
        sum += int(sys.argv[numbers])
    print(sum)
