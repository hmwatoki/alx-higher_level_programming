import unittest
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(10, 20, 30, 40, 1)
    def test_get_width(self):
        self.assertEqual(self.rectangle.get_width(), 10)
    def test_get_height(self):
        self.assertEqual(self.rectangle.get_height(), 20)
    def test_get_x(self):
        self.assertEqual(self.rectangle.get_x(), 30)
    def test_get_y(self):
        self.assertEqual(self.rectangle.get_y(), 40)
    def test_set_width(self):
        self.rectangle.set_width(15)
        self.assertEqual(self.rectangle.get_width(), 15)
    def test_set_width_raises_error(self):
        with self.assertRaises(TypeError):
            self.rectangle.set_width("15")
    def test_set_height(self):
        self.rectangle.set_height(25)
        self.assertEqual(self.rectangle.get_height(), 25)
    def test_set_height_raises_error(self):
        with self.assertRaises(TypeError):
            self.rectangle.set_height("25")
    def test_set_x(self):
        self.rectangle.set_x(35)
        self.assertEqual(self.rectangle.get_x(), 35)
    def test_set_x_raises_error(self):
        with self.assertRaises(TypeError):
            self.rectangle.set_x("35")
        with self.assertRaises(ValueError):
            self.rectangle.set_x(-5)
    def test_set_y(self):
        self.rectangle.set_y(45)
        self.assertEqual(self.rectangle.get_y(), 45)
    def test_set_y_raises_error(self):
        with self.assertRaises(TypeError):
            self.rectangle.set_y("45")
        with self.assertRaises(ValueError):
            self.rectangle.set_y(-5)
    
    def test_area(self):
        """Tests area"""
        r = Rectangle(4,7,1,4)
        expected_area = 4 * 7
        self.assertEqual(r.area(),expected_area)

    def test_display(self):
        """Tests display"""
        r = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as buffer:
            r.display()
            output = buffer.getvalue().strip()
        self.assertEqual(output, '###\n###')
        
if __name__ == '__main__':
    unittest.main()
