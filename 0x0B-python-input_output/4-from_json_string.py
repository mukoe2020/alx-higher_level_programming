#!/usr/bin/python3
"""Function converts a json string to python object"""
import json


def from_json_string(my_str):
    """python object will be presented as a json string"""
    return json.loads(my_str)
