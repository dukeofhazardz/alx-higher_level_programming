#!/usr/bin/python3
"""A function that returns an object (Python data structure)
    represented by a JSON string:"""
import json


def from_json_string(my_obj):
    """Returns the an object represented by a JSON string"""
    return (json.loads(my_obj))
