#!/usr/bin/python3

"""
Reads input from stdin line by line, parses each line, updates the 
total size and status codes, and prints metrics every 10 lines.
"""

import sys


def print_metrics(total_size, status_codes):
    """
    Prints the total file size and counts of each status code.

    :param total_size: An integer representing the total size of the file.
    :param status_codes: A dictionary containing the counts of each status code.
    :type total_size: int
    :type status_codes: dict
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """
    Parses a single line of log data to extract the status code and size.

    :param line: A string representing a single line of log data.
    :param total_size: The current total size of log data processed.
    :param status_codes: A dictionary containing the count of each status code encountered.
    :type line: str
    :type total_size: int
    :type status_codes: dict

    :return: A tuple containing the updated total size and status code count dictionary.
    :rtype: Tuple[int, dict]
    """
    try:
        fields = line.split()
        size = int(fields[-1])
        code = fields[-2]
        total_size += size
        if code in status_codes:
            status_codes[code] += 1
    except Exception:
        pass
    return total_size, status_codes


def main():
    """
    Reads input from stdin line by line, parses each line, updates the 
    total size and status codes, and prints metrics every 10 lines.
    """
    i = 0
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            i += 1
            total_size, status_codes = parse_line(line, total_size, status_codes)
            if i % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
