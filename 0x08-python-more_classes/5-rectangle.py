#!/usr/bin/python3
"""
class that defines a rectangle
"""


class Rectangle:
    """Representing the rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializing the rectangle

        Args:
        width: the width of the rectangle
        height: the height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting and setting private instance(width)"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getiing and setting private instance(height)"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of the rectangle"""

        """Checking if width or height is empty"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Printing representation of the rectangle, but with #"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_rows = []

        for h in range(self.__height):
            [rectangle_rows.append('#') for j in range(self.__width)]
            if h != self.__height - 1:
                rectangle_rows.append("\n")
        return "".join(rectangle_rows)

    def __repr__(self):
        """return a string representation of the rectangle"""

        rectangle_rows = "Rectangle(" + str(self.__width)
        rectangle_rows += ", " + str(self.__height) + ")"
        return rectangle_rows

    def __del__(self):
        """ Prints a message when an instance of rectangle is deleted"""
        print("Bye rectangle...")
