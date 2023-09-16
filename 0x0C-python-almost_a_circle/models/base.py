#!/usr/bin/python3
"""  the  bases class module """


import json


class Base:
    """
    Base class for representing a base object with a unique identifier (id).
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique identifier (id).

        Args:
        id (int, optional):unique identifier for the object (default is None).
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
        list_dictionaries (list):dictionaries to be converted to JSON string.

        Returns:
        str: The JSON string representation of the list of dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
        list_objs (list): List of instances that inherit from Base.

        Returns:
        None
        """

        filename = cls.__name__ + ".json"
        data = []

        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w") as file:
            file.write(cls.to_json_string(data))
