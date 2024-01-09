#!/usr/bin/python3
"""Define a class checking function"""


def is_kind_of_class(obj, a_class):
    """if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class
        False otherwise.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
