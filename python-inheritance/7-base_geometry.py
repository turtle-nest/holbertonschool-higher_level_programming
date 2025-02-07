#!/usr/bin/python3
"""
Module containing the BaseGeometry class.
"""

class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Throws an exception indicating that this method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a strictly positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
