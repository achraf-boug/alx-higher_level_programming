#!/usr/bin/python3
"""Def a text file insertion fun."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given str in a f.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
