#!/usr/bin/python3
"""Defining a function that checks if an obj is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
    obj: the object to be checked
    a_class: the specified class

    Return: True if the obj is an instance of the class
            False if otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
