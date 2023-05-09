#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_cd = ord(c)
        if ascii_cd >= 97 and ascii_cd <= 122:
            uppercase_cde = ascii_cd - 32
            c = chr(uppercase_cde)
        print("{}".format(c), end='')
    print()
