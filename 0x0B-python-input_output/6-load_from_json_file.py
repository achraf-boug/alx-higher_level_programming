#!/usr/bin/python3
"""Def a JSON file-reading fun."""
import json


def load_from_json_file(filename):
    """Create a Py obj from a JSON f."""
    with open(filename) as f:
        return json.load(f)
