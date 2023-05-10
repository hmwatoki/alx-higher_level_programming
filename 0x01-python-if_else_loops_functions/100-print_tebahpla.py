#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    if i % 2 == 1:
        print("{}".format(chr(i).lower()), end="")
    else:
        print("{}".format(chr(i).upper()), end="")
