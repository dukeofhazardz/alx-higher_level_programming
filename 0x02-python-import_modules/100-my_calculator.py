#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    length = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)

    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)), end="\n")
