#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_with_single_values(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

        self.assertEqual(max_integer([-1]), -1)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_duplicate_number(self):
        result = max_integer([10, 10, 10, 10, 10])
        self.assertEqual(result, 10)

    def test_with_mixed_int(self):
        result = max_integer([11111, 20, 0, -1234, -902, -2344])
        self.assertEqual(result, 11111)

        result = max_integer([-15, -20, 0, -1234, -902, -0])
        self.assertEqual(result, 0)

    def test_large_numbers(self):
        result = max_integer([1000000, 10000000, 1000000000])
        self.assertEqual(result, 1000000000)

    def test_zero(self):
        result = max_integer([0, 0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_negative_numbers(self):
        self.assertEqual(max_integer([-6]), -6)

    def test_only_one_negative_numbers(self):
        self.assertEqual(max_integer([-6, 1, 2]), 2)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
