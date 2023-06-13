#!/usr/bin/python3
"""Defines function read_file"""
def read_file(filename=""):
    """
    A function that reads the contents of a file and prints it to the console.

    Args:
        filename (str): The name or path of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open (filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content)
