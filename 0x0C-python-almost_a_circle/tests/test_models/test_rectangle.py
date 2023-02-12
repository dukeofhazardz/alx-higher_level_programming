#!/usr/bin/python3
"""Defines the test class for rectangle.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_Instantiation(unittest.TestCase):
    """Unittests for testing the instantiation of the Rectangle class"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(12)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(10, 11, 3)
        r2 = Rectangle(9, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(10, 11, 3, 7)
        r2 = Rectangle(9, 5, 6, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        r2 = Rectangle(9, 5, 6, 5, 3)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 3)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 11, 3, 7, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 11, 3, 7, 5).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 11, 3, 7, 5).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 11, 3, 7, 5).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 11, 3, 7, 5).__y)

    def test_width_getter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        self.assertEqual(r1.width, 10)

    def test_width_setter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        r1.width = 15
        self.assertEqual(r1.width, 15)

    def test_height_getter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        self.assertEqual(r1.height, 11)

    def test_height_setter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        r1.height = 19
        self.assertEqual(r1.height, 19)

    def test_x_getter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        self.assertEqual(r1.x, 3)

    def test_x_setter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        r1.x = 5
        self.assertEqual(r1.x, 5)

    def test_y_getter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        self.assertEqual(r1.y, 7)

    def test_y_setter(self):
        r1 = Rectangle(10, 11, 3, 7, 5)
        r1.y = 9
        self.assertEqual(r1.y, 9)





if __name__ == "__main__":
    unittest.main(verbosity=2)
