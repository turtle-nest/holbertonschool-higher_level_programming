#!/usr/bin/python3
""" Function to serialize an object to JSON-compatible dictionary
"""

def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
        (list, dictionary, string, integer, boolean)
        for JSON serialization of an object.
    """
    return obj.__dict__
