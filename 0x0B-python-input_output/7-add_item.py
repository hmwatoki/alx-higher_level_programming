#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then saves them to a file.
"""
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, filename)
