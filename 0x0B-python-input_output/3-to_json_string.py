#!/usr/bin/python3
"""
Converts a Python object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """returns a json string"""
    return json.dumps(my_obj)
