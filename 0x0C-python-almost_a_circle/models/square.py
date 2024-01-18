#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
class Square(Rectangle):  # Corrected class name to "Square"

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, x, y, id)  # Removed "self" inside super() and fixed indentation

    @property
    def size(self):  # Corrected indentation and added missing colon
        return self.width

    @size.setter
    def size(self, value):  # Corrected indentation and added missing colon
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method
        Args:
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2
        self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

"""Assuming the Rectangle class is defined somewhere in the code"""
class Rectangle:
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
