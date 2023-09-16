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
        """Passing negative height value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-23, 10)

        """Passing 0 width value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 0)

    def test_by_passing_neg_x_and_y(self):
        """Passing negative x value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 10, -2)

        """Passing negative y value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(23, 10, 0, -34)

    def test_by_passing_all_arguments(self):
        """Passing all arguments with id"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_by_passing_all_neg_arguments(self):
        """Passing all negative arguments with negative id"""
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, -2, -2, -4, -12)

    def test_invalid_types(self):
        """Testing invalid width type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("I'm here", (23, 45))

        """Testing invalid height type"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2.56)

        """Testing invalid x type"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, "I'm here")

        """Testing invalid y type"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 5, {'car': 'Tesla'})

    def test_if_None_is_passed(self):
        """Testing None width type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 2)

        """Testing None height type"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, None)

        """Testing None x type"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, None)

        """Testing None y type"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 5, None)

    def test_if_Bool_is_passed(self):
        """Testing Boolean width type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 2)

        """Testing None height type"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, False)

        """Testing None x type"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, False)

        """Testing None y type"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 5, True)
