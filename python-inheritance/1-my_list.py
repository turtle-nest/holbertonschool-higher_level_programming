#!/usr/bin/python3
"""
Module containing the MyList class.
"""

class MyList(list):
    """Class that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Displays the list sorted in ascending order."""
        print(sorted(self))
