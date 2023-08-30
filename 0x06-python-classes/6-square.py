#!/usr/bin/python3
"""6-square.py"""


class Square:
    """The class Square defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ is a special method.

        Args:
            size (int): this is a private instance attribute.
            position (tuple): this is a private instance attribute.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """The getter property retrieves the position.

        Args:
            value (int): it is the new position to be set using setter.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not (isinstance(x, int) and isinstance(y, int)) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This calculates the area of the Square.

        Args:
            cal (int): calculates area of a square.
        """
        cal = self.__size * self.__size
        return cal

    def my_print(self):
        """Prints to the stdout the square with character #.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
