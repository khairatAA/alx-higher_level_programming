#!/usr/bin/python3
"""base module"""


class Base:
    """This class will be the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor of the Base class
        Args:
            id: public instance attribute, holds the argument value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
