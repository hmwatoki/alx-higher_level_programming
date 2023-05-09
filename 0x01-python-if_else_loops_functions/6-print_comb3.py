#!/usr/bin/python3
for i in range(10):
    for a in range(i + 1, 10):
        print("{:d}{:d}".format(i, a), end="")
        if i < 8:
            print(", ", end="")
print()
