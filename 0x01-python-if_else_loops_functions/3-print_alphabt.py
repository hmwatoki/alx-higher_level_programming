#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) in ['q', 'e']:
        continue
    print("{:c}".format(i), end="")
