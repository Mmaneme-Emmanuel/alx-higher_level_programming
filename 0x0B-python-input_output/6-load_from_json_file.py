#!/usr/bin/python3
"""function that creates an Object"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”:"""
    with open(filename) as f:
        return json.load(f)
