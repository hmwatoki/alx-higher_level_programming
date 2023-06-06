#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an interger or float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an interger or float")
    a = int(a)
    b = int(b)
    return a + b