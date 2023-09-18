#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle
"""Rectangle class module importation"""


class Square(Rectangle):
    """The class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor for the Square class
        Args:
            size(int): the height or width of the square
            x(int): the x coordinate
            y(int): y coordinates
            id(int): the id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This is the public getter ans setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter.
        Args:
            value: the value to be set for width
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int or value is None:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """The String representation of the Square class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width))
