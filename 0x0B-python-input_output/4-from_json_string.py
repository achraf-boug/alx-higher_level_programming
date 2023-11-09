#!/usr/bin/python3
# 6-from_json_string.py
"""Def a JSON-to-object fun."""
import json


def from_json_string(my_str):
    """Ret the Py obj representation of a JSON str."""
    return json.loads(my_str)
