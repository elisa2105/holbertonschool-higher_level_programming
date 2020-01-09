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
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the attributes of an instance
        Args:
            size: Positive integer nuimbner asociated to the size
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of square
        """
        return self.size * self.size

    @property
    def size(self):
        """Accessor to a private instance
        Args:
            self: the instance of a square
        Returns:
            the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Mutator to a private instance
        Args:
            value: Integer value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Initializes private instance
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Mutator of private instance attribute position.
        Args:
            value: Integer
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Prints the information about square
        """
        if self.size == 0:
            print()
            return
        if self.position:
            for column in range(self.position[1]):
                print()
        for row in range(self.size):
            print("{}{}".format(" " * self.position[0], '#' * self.size))
