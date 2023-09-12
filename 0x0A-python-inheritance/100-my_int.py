#!/usr/bin/python3
"""Defines a class MyInt that inherits  from int"""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """Override == with !="""
        return self.real != value

    def __ne__(self, value):
        """Overrride != with == behavior """
        return self.real == value
