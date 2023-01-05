#!/usr/bin/python3

if __name__ == "__main__":

	from calculator_1 import add, sub, mul, div
	import sys

	length = len(sys.argv) - 1

	if length < 3:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
		sys.exit(1)
	if sys.argv[2] != '+' or sys.argv[2] != '-' or sys.argv[2] != '*' or sys.argv[2] != '/':
		print("Unknown operator. Available operators: +, -, * and /", end="\n")
		sys.exit(1)

	a = int(sys.argv[1])
	b = int(sys.argv[3])


	if sys.argv[2] == '+':
		print("{} + {} = {}".format(a, b, add(a, b)), end="\n")
	elif sys.argv[2] == '-':
		print("{} - {} = {}".format(a, b, sub(a, b)), end="\n")
	elif sys.argv[2] == '/':
		print("{} / {} = {}".format(a, b, div(a, b)), end="\n")
	elif sys.argv[2] == '*':
		print("{} * {} = {}".format(a, b, mul(a, b)), end="\n")
