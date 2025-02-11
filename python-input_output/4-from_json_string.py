#!/usr/bin/python3
"""Description of the module"""
import json

def from_json_string(my_str):
    """Returns the Python object represented by a JSON string."""
    return json.loads(my_str)
