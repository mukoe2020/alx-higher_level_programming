#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for h in x:
            print("{:d}".format(h), end=" " if h != x[-1] else "")
        print()
