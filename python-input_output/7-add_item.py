#!/usr/bin/python3
"""Description here"""
import sys
import importlib.util

# Dynamically import save_to_json_file from 5-save_to_json_file.py
spec = importlib.util.spec_from_file_location(
    "save_to_json_file", "./5-save_to_json_file.py"
)
save_to_json_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(save_to_json_file)

# Dynamically import load_from_json_file from 6-load_from_json_file.py
spec = importlib.util.spec_from_file_location(
    "load_from_json_file", "./6-load_from_json_file.py"
)
load_from_json_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(load_from_json_file)

def main():
    """
    A script that adds all command-line arguments to a Python list and saves 
    the list as a JSON representation to a file named 'add_item.json'.
    
    - If the file already exists, the arguments will be appended to the list 
    in the file.
    - If the file doesn't exist, it will be created and contain the list 
    of arguments.
    """
    filename = "add_item.json"

    # Try to load existing data from the file, or create an empty list if 
    # the file doesn't exist
    try:
        items = load_from_json_file.load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add all arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file.save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
