#!/usr/bin/python3
"""rectangle module"""
from models.base import Base
""" Base class module"""


class Rectangle(Base):
    """The class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the class constructor.
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: x coordinates
            y: y coordinates
            id: Call the super class with id
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """This is the public getter ans setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter"""
        self.__width = value

    @property
    def height(self):
        """This is the public getter ans setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter"""
        self.__height = value

    @property
    def x(self):
        """This is the public getter ans setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The x setter"""
        self.__x = value

    @property
    def y(self):
        """This is the public getter ans setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The y setter"""
        self.__y = value
