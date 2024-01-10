#!/usr/bin/python3
"""Define a class checking function"""


def inherits_from(obj, a_class):
    """if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class
        False otherwise.
    """

    if issubclass(type(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
