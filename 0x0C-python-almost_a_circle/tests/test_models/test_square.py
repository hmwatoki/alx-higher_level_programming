#!/usr/bin/python3
"""Unit test for square module"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test init method"""
    def test_init(self):
        """
        Initializes a square object with a specified width.
        :param self: The square object.
        :return: None.
        """
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_str(self):
        """
        Initializes a Square object.
        Calls the __str__ method of Square class
        checks if it returns the expected string.
        """
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")


if __name__ == '__main__':
    unittest.main()
