#!/usr/bin/python3
"""Defines a function to print a sorted list"""


class MyList(list):
    """Impliments sorted list"""
    def print_sorted(self):
        """
        Sorts the elements in the object and prints them in ascending order.

        :param self: The object to be sorted and printed.
        :return: None
        """
        sorted_list = sorted(self)
        print(sorted_list)
