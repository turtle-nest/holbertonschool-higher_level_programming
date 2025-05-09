#!/usr/bin/python3
"""This module defines a class Square that represents a square."""

class Square:
    """Represents a square with a size and calculates its area."""

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

    @property
    def size(self):
        """
        Getter for the size property.

        Returns:
            self.__size: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size property.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If 'value' is not an integers.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position property.

        Returns:
            self.__position: The position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position property.

        Args:
            value (tuple): The new position to set.

        Raises:
            TypeError: If value is not a tuple of two integers
        """
        if (
            not isinstance(value, tuple)
            or tuple != 2
            or not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the symbol #

        Return:
            None
        """
        if self.__size == 0:
            print()

        # Print the vertical offset (position[1])
        print("\n" * self.__position[1], end="")

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
