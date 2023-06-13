#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    def __eq__(self, other):
        """
        Check if the current object is equal to another object by comparing it with the other object using the '!=' operator.

        :param other: The other object to compare this object to.
        :type other: any
        :return: True if the current object is not equal to the other object, False otherwise.
        :rtype: bool
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        This function checks if the object is not equal to another object by utilizing the
        `__eq__` method of the parent class.

        :param self: The object that the method is called upon.
        :param other: The object to compare with.
        :return: The result of the comparison between the two objects.
        :rtype: bool
        """
        return super().__eq__(other)
