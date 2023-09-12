#!/usr/bin/python3
""""
a module that writes that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename="", txt=""):
    """
    reading the string
    """

    with open(filename, encoding="utf-8") as i:
        print(i.read(), end="")
