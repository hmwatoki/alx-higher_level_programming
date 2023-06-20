#!/usr/bin/python3
"""Rectangle test module"""
import unittest
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch


class TestRectangle(unittest.TestCase):

    def setUp(self):
        """
        Initializes the test fixture with a rectangle object.

        :param self: The test fixture.
        :return: None.
        """

        self.rectangle = Rectangle(10, 20, 30, 40, 1)

    def test_get_width(self):
        """Test width getter"""
        self.assertEqual(self.rectangle.get_width(), 10)

    def test_get_height(self):
        """Test height getter"""
        self.assertEqual(self.rectangle.get_height(), 20)

    def test_get_x(self):
        """Test x value getter"""
        self.assertEqual(self.rectangle.get_x(), 30)

    def test_get_y(self):
        """Test y value getter"""
        self.assertEqual(self.rectangle.get_y(), 40)

    def test_set_width(self):
        """Test width getter"""
        self.rectangle.set_width(15)
        self.assertEqual(self.rectangle.get_width(), 15)

    def test_set_width_raises_error(self):
        """Test width with error"""
        with self.assertRaises(TypeError):
            self.rectangle.set_width("15")

    def test_set_height(self):
        """Test height getter"""
        self.rectangle.set_height(25)
        self.assertEqual(self.rectangle.get_height(), 25)

    def test_set_height_raises_error(self):
        """Test height with error"""
        with self.assertRaises(TypeError):
            self.rectangle.set_height("25")

    def test_set_x(self):
        """Test x value getter"""
        self.rectangle.set_x(35)
        self.assertEqual(self.rectangle.get_x(), 35)

    def test_set_x_raises_error(self):
        """Test x with error"""
        with self.assertRaises(TypeError):
            self.rectangle.set_x("35")
        with self.assertRaises(ValueError):
            self.rectangle.set_x(-5)

    def test_set_y(self):
        """Test y value getter"""
        self.rectangle.set_y(45)
        self.assertEqual(self.rectangle.get_y(), 45)

    def test_set_y_raises_error(self):
        """Test y with error"""
        with self.assertRaises(TypeError):
            self.rectangle.set_y("45")
        with self.assertRaises(ValueError):
            self.rectangle.set_y(-5)

    def test_area(self):
        """Tests area"""
        r = Rectangle(4, 7, 1, 4)
        expected_area = 4 * 7
        self.assertEqual(r.area(), expected_area)

    def test_display(self):
        """Tests display"""
        r = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as buffer:
            r.display()
            output = buffer.getvalue().strip()
        self.assertEqual(output, '###\n###')

    def test_str(self):
        """Tests __str__ method"""
        r = Rectangle(7, 4, 1, 3)
        output = str(r)
        self.assertEqual(output, '[Rectangle] ({}) 1/3 - 7/4'.format(r.id))


if __name__ == '__main__':
    unittest.main()
