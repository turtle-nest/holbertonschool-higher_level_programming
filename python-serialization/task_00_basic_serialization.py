#!/usr/bin/python3
"""Basic serialisation module"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    If the file already exists, it will be replaced.
    
    Args:
        data: Dictionary to serialize
        filename: Name of the output JSON file
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.
    
    :param filename: Name of the input JSON file
    :return: Deserialized dictionary
    """
    with open(filename, "r") as file:
        return json.load(file)
