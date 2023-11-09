#!/usr/bin/python3
"""Def a string-to-JSON fun."""
import json


def to_json_string(my_obj):
    """Ret the JSON representation of a str obj."""
    return json.dumps(my_obj)
