#!/usr/bin/python3
"""Description of the module"""
import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
    filename: The name of the file containing the JSON string.
    
    Returns:
    The Python object represented by the JSON string.
    """
    with open(filename, 'r') as file:
        return json.load(file)
