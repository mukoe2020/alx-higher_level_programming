#!/usr/bin/pythom3
def matrix_divided(matrix, div):
    """
    this module divides a matrix by div
    elements of a matrix should be divided by div rounded to 2 decimal places

    args:
    matrix (a list of numbers either float or integers)
    div (it's an integer or float)

    raises:
    TypeError: if a matrix or div is not an integer or float
    TypeError: if a matrix is not the same size
    ZeroDivisionError: if div is equal to zero

    returns:
    a new matrix
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
