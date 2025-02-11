#!/usr/bin/python3
"""Module to reading data from one format (CSV)
and converting it into another format (JSON) using serialization techniques"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and writes the output to data.json.
    
    Args:
        csv_filename (str): The name of the CSV file to convert.
    
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
