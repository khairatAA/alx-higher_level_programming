#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Importing unittest, Base and Rectangle modules"""


class TestBase(unittest.TestCase):
    """Runs test for the Rectangle class"""
    def test_inheritance(self):
        """Check if Rectangle Class is a subclass of Base Class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_by_passing_hight_and_width(self):
        """Passing only heights and width"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_by_passing_neg_hight_and_width(self):
        """Passing only negative heights and width"""
        r2 = Rectangle(-10, -2)
        self.assertEqual(r2.id, 2)

    def test_by_passing_all_arguments(self):
        """Passing all arguments with id"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_by_passing_all_neg_arguments(self):
        """Passing all negative arguments with negative id"""
        r4 = Rectangle(-10, -2, -2, -4, -12)
        self.assertEqual(r4.id, -12)
