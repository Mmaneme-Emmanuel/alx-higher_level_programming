#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
            position (tuple): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("Position must be a tuple of 2 positive integers")

        # Check if the tuple has exactly 2 elements
        if len(value) != 2:
            raise TypeError("Position must be a tuple of 2 positive integers")

        # Check if both elements in the tuple are positive integers
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("Position must be a tuple of 2 positive integers")

        # If all checks pass, the position is valid
        self._position = value

    def area(self):
        """Returns the current square area."""
        return self._size * self._size

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._size):
                print(" " * self._position[0], end="")
                print("#" * self._size)
