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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            cls: class instance
            list_objs: is a list of instances who inherits of Base
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            to_str = "[]"
        else:
            to_dict_list = []
            for i in list_objs:
                to_dict_list.append(i.to_dictionary())
            to_str = cls.to_json_string(to_dict_list)

        with open(file_name, 'w', encoding="utf-8") as file:
            written_str = file.write(to_str)

        return written_str

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string: is a string representing a list of dictionaries
        """
        to_str = []
        if json_string is None or len(json_string) == 0:
            return to_str
        else:
            to_str = json.loads(json_string)
            return to_str

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            cls: class instance
            dictionary: arbituary keyworded argument, representing a dict
        """
        dummy_instance = cls(1, 1)

        dummy_instance.update(**dictionary)

        return dummy_instance
