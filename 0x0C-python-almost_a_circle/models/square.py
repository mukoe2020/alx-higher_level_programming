#!/usr/bin/python3
"""Defining a class square, inheriting from the class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    Represents a square shape with equal width and height.

    Attributes:
    size (int): The size (width/height) of the square.
    x (int): The x-coordinate of the square's position.
    y (int): The y-coordinate of the square's position.
    id (int): The unique identifies the square inherited from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance

        Raises:
        TypeError: If size, x, or y is not an integer.
        ValueError: If size, x, or y is less than 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Set for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a formatted string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the square.

        Args:
        *args: representing positional arguments.
        **kwargs:representing attribute key-value pairs.
        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.

        Returns:
        dict: The dictionary representing the square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
