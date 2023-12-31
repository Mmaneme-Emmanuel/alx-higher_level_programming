#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (unit): the size of the new square.
        """
        self._size = size

    @property
    def size(self):
        """get/set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """returns the current square area."""
        return (self._size * self._size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(0, self._size):
            [print("#", end="") for j in range(self._size)]
            print("")
        if self._size == 0:
            print("")
