#!/usr/bin/python3
"""
a function that creates an object from json file
"""
import json


def load_from_json_file(filename):
    """
    creating an object from json file
    """
    with open(filename) as i:
        return json.load(i)
