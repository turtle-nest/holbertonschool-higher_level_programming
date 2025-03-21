#!/usr/bin/python3
"""
Module containing the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
        
        The size is validated using integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
