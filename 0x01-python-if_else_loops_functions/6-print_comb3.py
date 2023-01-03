#!/usr/bin/python3

'''A program that prints all possible different combinations of two digits.
   01 and 10 are considered the same combination of the two digits 0 and 1'''

for number1 in range(0, 10):
    for number2 in range(number1 + 1, 10):
        if number1 == 8 and number2 == 9:
            print("{}{}".format(number1, number2))
        else:
            print("{}{}".format(number1, number2), end=", ")
