#!/usr/bin/python3
"""Define a class checking function"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class, otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
