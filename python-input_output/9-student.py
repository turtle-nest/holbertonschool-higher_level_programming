#!/usr/bin/python3
"""Module that represent a student"""

class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance. 

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def to_json(self):
        """Return the dictionnary of the instance."""
        return self.__dict__
