#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    length = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3])i
    c = sys.argv[2]

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        sys.exit(1)

    if c not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        sys.exit(1)

    print("{} {} {} = {}".format(a, c, b, ops[c](a, b)), end="\n")
