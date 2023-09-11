#!/usr/bin/python3
"""
 A class MyList that inherits from list
"""


class MyList(list):
    """ a method that prints the list but sorts it out"""
    def print_sorted(self):
        print(sorted(self))
