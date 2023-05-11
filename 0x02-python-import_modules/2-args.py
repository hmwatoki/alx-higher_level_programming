#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arglen = len(sys.argv) - 1
    args = sys.argv[1:]
    plural = "s" if arglen > 1 else ""
    print("{:d} argument{:s}{}"
          .format(arglen, plural, ":" if arglen else "."))
    for i, arg in enumerate(args):
        print("{:d}: {}".format(i + 1, arg))
