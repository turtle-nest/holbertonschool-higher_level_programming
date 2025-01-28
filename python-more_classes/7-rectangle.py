#!/usr/bin/python3
"""This module defines a class Rectangle that represent a rectangle"""

class Rectangle:
    """Represents a rectangle with a width and an height."""

    number_of_instances = 0
    print_symbol = "#"

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
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns: 
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__ (self):
        """
        Returns a string representation of the rectangle
        with the character print_symbol.

        Returns:
            str: The rectangle in string form or an empty string
            if width or height is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width
            rectangle_str += "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle to recreate it.

        Returns:
            str: A string in the format Rectangle(width, height).
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
