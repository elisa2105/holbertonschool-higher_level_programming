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
            size (int): Positive number given to the size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
