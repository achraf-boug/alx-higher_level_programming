#!/usr/bin/python3
"""Def a JSON file-writing fun."""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to a text f using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
