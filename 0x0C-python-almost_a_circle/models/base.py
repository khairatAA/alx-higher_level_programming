#!/usr/bin/python3
"""base module"""
import json
"""import json module"""


class Base:
    """This class will be the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor of the Base class
        Args:
            id: public instance attribute, holds the argument value
            __nb_objects: increments as instances are created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries(dict): list of dictionary
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string
