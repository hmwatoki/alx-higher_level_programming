#!/usr/bin/python3
"""Defines function read_file"""


def read_file(filename=""):
    """
    A function that reads the contents of a file

    Args:
        filename(str):The name or path of the file to read.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
