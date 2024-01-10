#!/usr/bin/python3
"""Defining a BaseGeometry function"""


class BaseGeometry:
    """A class of basegeometry"""

    def area(self):
        """Public instance method that raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as integer
        Args:
            name(str) name of parameter
            value(int) the parameter to validate
        Raise:
            TypeError:if value is not an integer
            ValueError: if value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
