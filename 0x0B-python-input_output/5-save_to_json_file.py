#!/usr/bin/python3
"""
A function that writes an Object to a text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """writing object to the text file"""
    with open(filename, "w", encoding="utf-8") as i:
        json.dump(my_obj, i)
