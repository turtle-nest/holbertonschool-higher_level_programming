#!/usr/bin/python3
"""Description of the module"""
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
