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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If `attrs` is a list of strings, only those attributes are
        retrieved. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    Defaults to None.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary where keys match public attributes
                         and values replace the current attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
