#!/usr/bin/python3
"""
the function will create a new matrix to store the row square
the for loop will iterate the numbers in a row creating squares
"""


def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        row_squared = []
        for num in row:
            squared_num = num * num
            row_squared.append(squared_num)
        new_matrix.append(row_squared)

    return new_matrix
