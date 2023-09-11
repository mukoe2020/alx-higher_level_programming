#!/usr/bin/python3

"""
A function that checks whether the object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Args:
    obj: the object to be checked
    a_class: the class to match the type of instance

    Return: True if obj is an instance of a_class
             Otherwise - False
    """

    if type(obj) == a_class:
        return True
    return False
