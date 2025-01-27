#!/usr/bin/python3
"""This module defines a square with a private attribut size"""

class Square:
    """Represents a square"""

    def __init__(self, size):
        """
        Initializes the square with a private attribut size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
