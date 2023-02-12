#!/usr/bin/python3
"""Defines unittests for base.py"""
import os
import unittest
from models.base import Base


class BaseTest_Instantiation(unittest.TestCase):
    """Unittest for testing the instantiation of the base class"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        
    def test_unique_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_instance_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        b1 = Base(12)
        b1.id = 15
        self.assertEqual(b1.id, 15)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual(Base("hello").id, "hello")




if __name__ == "__main__":
    unittest.main()
