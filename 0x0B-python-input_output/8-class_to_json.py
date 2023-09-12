#!/usr/bin/python3
"""
module defines a python class to json function
"""


def class_to_json(obj):
    """
    returning the dict representation of the obj
    """
    return obj.__dict__
