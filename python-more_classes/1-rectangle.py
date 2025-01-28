#!/usr/bin/python3
"""This module defines a class Rectangle that represent a rectangle"""

class Rectangle:
    """Represents a rectangle with a width and an height."""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises: 
            TypeError: If width or height are not integers.
            ValueError: If width or height are negatives.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """
        Getter for the width property.

        Returns:
            self.__width: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width property.

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If 'value' is not an integers.
            ValueError: If 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height property.

        Returns:
            self.__height: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height property.

        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If 'value' is not an integers.
            ValueError: If 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
