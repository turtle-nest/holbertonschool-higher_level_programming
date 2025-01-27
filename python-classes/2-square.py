#!/usr/bin/python3
"""This module describes a square by a private instance attribute size."""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """
        Initializes the square with a private instance attribute size.

        Args:
            size (int): The private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
