#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load the existing data from the file, or create an empty list if the file doesn't exist
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
