#!/usr/bin/python3
"""  the  bases class module """


class Base:
    """
    base class for managing id attribute

    attributus:
    __nb_objects: a private class atribute to intialize the bases
    """

    __nb_objects = 0
    """
    Args: the id  of the base
    if id not provided it is generated on __nb _object
    """
    def __init__(self, id=None):
        if id is not None:
            self .id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
