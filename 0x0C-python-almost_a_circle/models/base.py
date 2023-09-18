#!/usr/bin/python3
"""Defining a base class"""
import json
import turtle
import csv


class Base:
    """Representing the base class

    Attributes:
    __nb_objects: private class attribute for number of initialized bases
    """

    __nb_objects = 0

    """Initializing class
    Args:
    id: The id of the new base

    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the class"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [h.to_dictionary() for h in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        Reading from `<cls.__name__>.json`

        Returns: an empty list if the file does not exist
        Otherwwise a list of instances

        """

        f_name = str(cls.__name__) + ".json"
        try:
            with open(f_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from <cls.__name__>.csv.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
         staticmethod that opens a window and
         draws all the Rectangles and Squares:

         Args:
         list_rectangles: a list of rectangle objects drawn
         list_squares: a lost of square objects to be drawn

        """
        t_draw = turtle.Turtle()
        """Setting background color to dark gray"""
        t_draw.screen.bgcolor("#333333")
        """Setting thickness of the line"""
        t_draw.pensize(4)
        t_draw.shape("turtle")

        t_draw.color('black', 'purple')
        for rect in list_rectangles:
            t_draw.showturtle()
            t_draw.up()
            t_draw.goto(rect.x, rect.y)
            t_draw.down()
            for h in range(2):
                t_draw.forward(rect.width)
                t_draw.left(90)
                t_draw.forward(rect.height)
                t_draw.left(90)
            t_draw.hideturtle()

        """Drawing the squares"""
        t_draw.color('green', 'yellow')
        for sqr in list_squares:
            t_draw.showturtle()
            t_draw.up()
            t_draw.goto(sqr.x, sqr.y)
            t_draw.down()
            for m in range(2):
                t_draw.forward(sqr.width)
                t_draw.left(90)
                t_draw.forward(sqr.height)
                t_draw.left(90)
            t_draw.hideturtle()

        turtle.exitonclick()
