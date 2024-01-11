#!/usr/bin/python3
""" function that writes a string"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the char.
    Args:
        filename (str) this is the container file
        text (str) what to be writen in file
    Return:
        number of text written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
