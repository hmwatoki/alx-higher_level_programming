#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then saves them to a file.
"""
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    jsonList = load_from_json_file("add_item.json")
except:
    jsonList = []

for i in sys.argv[1:]:
    jsonList.append(i)
save_to_json_file(jsonList, "add_item.json")
