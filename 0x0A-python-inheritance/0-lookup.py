#!/usr/bin/python3
"""
Defining a function that returns the list of available attributes,
and methods of an object
"""


def lookup(obj):
    """returns the list of an objects available attributes"""
    return dir(obj)
