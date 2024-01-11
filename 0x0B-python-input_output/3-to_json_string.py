#!/usr/bin/python3
"""unction that returns the JSON """
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string):"""
    return json.dump(my_obj)
