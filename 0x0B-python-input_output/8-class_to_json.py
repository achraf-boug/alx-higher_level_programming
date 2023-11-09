#!/usr/bin/python3
"""Def a Py class-to-JSON fun."""


def class_to_json(obj):
    """Ret the dictionary represntation of a simple data struc."""
    return obj.__dict__
