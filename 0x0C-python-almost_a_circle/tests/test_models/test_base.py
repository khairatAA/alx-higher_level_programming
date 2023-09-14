#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
"""Importing the unittest module"""
from models.base import Base
"""Importing the base module were the Base class is"""


class TestBase(unittest.TestCase):
    """Runs test for the Bases class"""
    def test_when_id_is_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_with_args(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

        b2 = Base(123456)
        self.assertEqual(b2.id, 123456)

    def test_with_negative_args(self):
        b1 = Base(-12)
        self.assertEqual(b1.id, -12)

        b2 = Base(-9)
        self.assertEqual(b2.id, -9)

    def test_with_zero_as_args(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)
