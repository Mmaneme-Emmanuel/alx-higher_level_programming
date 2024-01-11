#!/usr/bin/python3
# 6-from_jason_string.py
"""unction that returns the JSON """
import json


def from_json_string(my_str):
    """returns the JSON representation of an object (string):"""
    return json.loads(my_str)
