#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """private class attribute initialized to 0"""
    __nb_objects = 0

    """class constructor"""
    def __init__(self, id=None):
        """if id is not None, assign it to public instance attribute id
        otherwise, increment __nb_objects and assign the new value to id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            file_json = "[]"
        else:
            file_json = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            filename = cls.__name__ + ".json"
            with open(filename, 'w') as file:
                file.write(file_json)

    @staticmethod
    def from_json_string(json_string):
        """Update the class Base by adding the static method."""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base by adding the class method."""
        instance = cls.__new__(cls)
        if cls.__name__ == "Rectangle":
            instance.width = 0
            instance.height = 0
        elif cls.__name__ == "Square":
            instance.size = 0
        instance.update(**dictionary)
        return instance
