#!/usr/bin/python3
""" Defines a Square
Attributes:
    None
"""


class Square:
    """Creates a class Square given a size
    Attributes:
        None
    """
    def __init__(self, size=0):
        """Initializes the attributes of an instance
        Args:
            size (int): Positive number asociated to size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Accessor to the private instance size
        Args:
            self: the instance of a square
        Returns:
            the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Mutator to the private instance size
        Args:
            value: integer with the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
