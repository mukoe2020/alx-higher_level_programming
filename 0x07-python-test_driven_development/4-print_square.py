#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    A function that prints a square with # characters.

    Args:
        size (int): The size length of the square.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for h in range(size):
        print("#" * size)
