#!/usr/bin/python3

"""A function that converts a Roman numeral to an integer."""


def value(n):
    if (n == 'I'):
        return 1
    if (n == 'V'):
        return 5
    if (n == 'X'):
        return 10
    if (n == 'L'):
        return 50
    if (n == 'C'):
        return 100
    if (n == 'D'):
        return 500
    if (n == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    if (roman_string and isinstance(roman_string, str)):
        
        res = i = 0

        while (i < len(roman_string)):
            # Getting the value of symbol roman_string[i]
            s1 = value(roman_string[i])
            if (i + 1 < len(roman_string)):
                # Getting the value of symbol roman_string[i+1]
                s2 = value(roman_string[i + 1])
                # Comparing both values
                if (s1 >= s2):
                    # Value of currrent symbol is greater or
                    # equal to the next symbol
                    res = res + s1
                    i = i + 1
                else:
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    res = res + s2 - s1
                    i = i + 2
            else:
                res = res + s1
                i = i + 1

        return res
    else:
        return 0
