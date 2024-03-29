#!/usr/bin/python3
"""Defining function that reads a text file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
