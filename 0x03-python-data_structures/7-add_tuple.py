#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend the tuples to have a minimum length of 2 by adding 0's
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Extract the first two elements from each tuple and add them
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    return sum_first, sum_second
