#!/usr/bin/python3
"""102-square.py"""


class Square:
    """The class Square defines a square."""
    def __init__(self, size=0):
        """The __init__ is a special method.

        Args:
            size (int): this is a private instance attribute.
        """
        self.__size = size

    @property
    def size(self):
        """This is the getter property used to retrieve size.

        Args:
            value (int): the variable in the setter property the holds the new
            size value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This calculates the area of the Square.

        Args:
            cal (int): calculates area of a square.
        """
        cal = self.__size * self.__size
        return cal

    def __eq__(self, other):
        """Compaires with equality"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compaires with not equal to"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compaires with greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compaires with greater than or equal to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compaires with less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compaires with less than or equal to"""
        return self.area() <= other.area()
