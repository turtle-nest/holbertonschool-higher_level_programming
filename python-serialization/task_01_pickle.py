#!/usr/bin/python3
"""Serialize and deserialize custom Python objects using the pickle module."""

import pickle

class CustomObject:
    """A custom class to demonstrate pickling in Python."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name =name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error : {e}")
            return None
