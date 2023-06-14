#!/usr/bin/python3
"""appends text to a file"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    :param filename: The name of the file to append the text to.
    :type filename: str
    :param text: The text to append to the file.
    :type text: str
    :return: The number of characters written to the file.
    :rtype: int
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
