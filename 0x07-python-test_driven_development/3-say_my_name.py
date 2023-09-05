#!/usr/bin/python3
"""
Module contains a function which prints out a name/message
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints out My name is <first name> <last name>

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Returns:
        None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
