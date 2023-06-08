#!/usr/bin/python3
"""
This module contains functions for performing addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers together.

    Args:
        a: A number.
        b: second number.

    Returns:
        The sum of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an interger or float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an interger or float")
    a = int(a)
    b = int(b)
    return a + b
