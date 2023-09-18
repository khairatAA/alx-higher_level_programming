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

    def __str__(self):
        """The String representation of the Square class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width))
