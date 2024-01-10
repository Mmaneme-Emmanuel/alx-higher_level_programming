#!/usr/bin/python3
"""Defining a BaseGeometry function"""


class BaseGeometry:
    """A class of basegeometry"""

    def area(self):
        """Public instance method that raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self._name = name
        self._value = value

        if not isinstance(value, int):
            raise TypeError("{name} must be an integer")
        
        if  value <= 0:
            raise ValueError("{name} must be greater than 0")
