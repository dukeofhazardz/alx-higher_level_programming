#!/usr/bin/python3

def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix."""

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, int) or isinstance(ele, float)
            for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    elif (not(all(len(row) == len(matrix[0]) for row in matrix))):
        raise TypeError("Each row of the matrix must have the same size")

    elif (type(div) not in (int, float)):
        raise TypeError("div must be a number")

    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
