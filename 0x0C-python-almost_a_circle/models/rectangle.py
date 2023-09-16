#!/usr/bin/python3
from models.base import Base
"""
Rectangle class that inherits from the Base class.
"""


class Rectangle(Base):
    """
    Methods:
    __init__(self, width, height, x=0, y=0, id=None):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with width, height, position, and id.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the rectangle's position
        y (int, optional): The y-coordinate of the rectangle's position
        id (int, optional): The unique identifier for the rectangle

        Raises:
        TypeError: If width, height, x, or y is not an integer.
        ValueError: If width, height, x, or y is less than or equal to 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a formatted string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """
        Calculates and returns the area value of the rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle instance with the character '#'.
        """
        for _ in range(self.height):
            print("#" * self.width)

    def display(self):
        """
        Prints the Rectangle instance with '#' character
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """Getter for the x-coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x-coordinate attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """Getter for the y-coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y-coordinate attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value

    def update(self, *args, **kwargs):
        """Method that updates the rectangle class"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.

        Returns:
        dict: The dictionary representing the rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
