#!/usr/bin/python3
def uppercase(str):
    x = ""
    for i in str:
        if "a" <= i <= "z":
            x += chr(ord(i) - 32)
        else:
            x += i
    print(x)
