#!/usr/bin/python3

import sys

args = sys.argv[1:]
x = 1

print("{} arguments:".format(len(args)))

for arg in args:
    print("{}: {}".format(x, arg))
    x += 1
