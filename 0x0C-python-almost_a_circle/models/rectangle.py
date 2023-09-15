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

    def update(self, *args):
        """
        Assigns arguments to the attributes in the specified order

        Args:
        *args: Variable-length arguments in the specified order.
        """
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """
        Assigns a key/value argument to the attributes of the rectangle.

        Args:
        *args: Variable-length argument list representing positional arguments.
        This argument list is skipped if it exists and is not empty.
        **kwargs: Variable-lengt argument representing attribute key-value pairs.
        Each key represents an attribute of the rectangle.
        This argument type is known as a "keyworded argument".
        Argument order is not important.
        """
    if args and len(args) > 0:
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
    else:
        for key, value in kwargs.items():
            setattr(self, key, value)


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
