#!/usr/bin/python3
"""Defining function that appends a string"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8).

    Args:
        filename (str) where the appending will be done
        text (str) the words to be appended to filename

    Return:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
