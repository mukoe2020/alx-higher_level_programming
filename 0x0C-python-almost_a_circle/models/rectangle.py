#!/usr/bin/python3
"""Defining a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A new rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialzing the class
        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        x: the x coordinate of the rectangle
        y: the y coordinate of the rectangle
        id: represents the identity of the rectangle

        Raises:
        TypeError: if either width or height is not an int
        ValueError: if either width or height is <= 0
        TypeError: If either x or y is not an int
        ValueError: If either x or y is <= 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting and checking the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting and checking the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting and checking the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the class rectangle"""
        return self.__height * self.__width

    def display(self):
        """Displays the rectangle with the '#' character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for row in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for h in range(self.width)]
            print("")

    def __str__(self):
        """Override string representation of the class
        in the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Method that assigns arguments to each attribute
        Args:
        args: number of arguments
        - first argument represents the id attribute
        - second argument represents the width attribute
        - third argument represents the height attribute
        - fourth argument represents the x attribute
        - fifth argument represents the y attribute

        kwargs: represents args with a key = value format
        """

        if args and len(args) != 0:
            g = 0
            for arg in args:
                if g == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif g == 1:
                    self.width = arg
                elif g == 2:
                    self.height = arg
                elif g == 3:
                    self.x = arg
                elif g == 4:
                    self.y = arg
                g += 1

        elif kwargs and len(kwargs) != 0:
            """ assigning a key/value argument to attributes
            -   Argument order is not important.
            """

            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the class"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
