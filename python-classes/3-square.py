#!/usr/bin/python3
"""This module defines a class Square that represents a square."""

class Square:
    """Represents a square with a size and calculates its area."""

    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size (int): The size of one side of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
