#!/usr/bin/python3

"""
Rectangle test module
"""

import unittest
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """
    Tests for the Rectangle class
    """

    def setUp(self):
        """
        Initializes the test fixture with a rectangle object.
        """
        self.rectangle = Rectangle(10, 20, 30, 40, 1)

    def test_get_width(self):
        """
        Test width getter
        """
        self.assertEqual(self.rectangle.width, 10)

    def test_get_height(self):
        """
        Test height getter
        """
        self.assertEqual(self.rectangle.height, 20)

    def test_get_x(self):
        """
        Test x value getter
        """
        self.assertEqual(self.rectangle.x, 30)

    def test_get_y(self):
        """
        Test y value getter
        """
        self.assertEqual(self.rectangle.y, 40)

    def test_set_width(self):
        """
        Test width setter
        """
        self.rectangle.width = 15
        self.assertEqual(self.rectangle.width, 15)

    def test_set_width_raises_error(self):
        """
        Test width with error
        """
        with self.assertRaises(TypeError):
            self.rectangle.width = "15"

    def test_set_height(self):
        """
        Test height setter
        """
        self.rectangle.height = 25
        self.assertEqual(self.rectangle.height, 25)

    def test_set_height_raises_error(self):
        """
        Test height with error
        """
        with self.assertRaises(TypeError):
            self.rectangle.height = "25"

    def test_set_x(self):
        """
        Test x value setter
        """
        self.rectangle.x = 35
        self.assertEqual(self.rectangle.x, 35)

    def test_set_x_raises_error_type_error(self):
        """
        Test x with TypeError error
        """
        with self.assertRaises(TypeError):
            self.rectangle.x = "35"

    def test_set_x_raises_error_value_error(self):
        """
        Test x with ValueError error
        """
        with self.assertRaises(ValueError):
            self.rectangle.x = -5

    def test_set_y(self):
        """
        Test y value setter
        """
        self.rectangle.y = 45
        self.assertEqual(self.rectangle.y, 45)

    def test_set_y_raises_error_type_error(self):
        """
        Test y with TypeError error
        """
        with self.assertRaises(TypeError):
            self.rectangle.y = "45"

    def test_set_y_raises_error_value_error(self):
        """
        Test y with ValueError error
        """
        with self.assertRaises(ValueError):
            self.rectangle.y = -5

    def test_area(self):
        """
        Tests area
        """
        r = Rectangle(4, 7, 1, 4)
        expected_area = 4 * 7
        self.assertEqual(r.area(), expected_area)

    def test_display(self):
        """
        Tests display
        """
        r = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as buffer:
            r.display()
            output = buffer.getvalue().strip()
        self.assertEqual(output, '###\n###')

    def test_str(self):
        """
        Tests __str__ method
        """
        r = Rectangle(7, 4, 1, 3)
        output = str(r)
        self.assertEqual(output, '[Rectangle] ({}) 1/3 - 7/4'.format(r.id))

    def test_update(self):
        """Test update method"""
        # Test with no args
        self.rectangle.update()
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 30/40 - 10/20")

        # Test with one arg
        self.rectangle.update(2)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2) 30/40 - 10/20")

        # Test with two args
        self.rectangle.update(2, 15)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2) 30/40 - 15/20")

        # Test with three args
        self.rectangle.update(2, 15, 25)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2) 30/40 - 15/25")

        # Test with four args
        self.rectangle.update(2, 15, 25, 35)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2) 35/40 - 15/25")

        # Test with five args
        self.rectangle.update(2, 15, 25, 35, 45)
        self.assertEqual(str(self.rectangle), "[Rectangle] (2)35/45 -15/25")


if __name__ == '__main__':
    unittest.main()
