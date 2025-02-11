#!/usr/bin/python3
"""Module that explore serialization and deserialization
using XML as an alternative format to JSON."""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.
    
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a dictionary.
    
    Args:
        filename (str): The name of the XML file to deserialize.
    
    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
