#!/usr/bin/python3
"""Writes to a file"""
def write_file(filename="", text=""):
    """
    Writes the given text to the file with the given filename.
    
    :param filename: A string representing the file name.
    :param text: A string representing the text to be written.
    :return: An integer representing the number of characters.
    """
    with open(filename,mode='w',encoding='utf-8') as file:
        file.write(text)
        return len(text)
