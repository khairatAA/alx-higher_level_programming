#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_with_invalid_type(self):
        self.assertRaises(TypeError, max_integer, "1234")
        self.assertRaises(TypeError, max_integer, (123, "car", "Tesla"))
        self.assertRaises(TypeError, max_integer, 123.789)
        self.assertRaises(TypeError, max_integer, {'name': 'khairat'})

    def test_with_None(self):
        self.assertIsNone(max_integer())

    def test_empyt_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_with_list_of_dif_type(self):
        self.assertRaises(TypeError, max_integer, [1.5, 2.6, 4.8, 9.0])
        self.assertRaises(TypeError, max_integer, [1, 2, None, 4, 5])
        self.assertRaises(TypeError, max_integer, ['a', 'b', 1, 3])
        self.assertRaises(TypeError, max_integer, ['a', ['b'], 1, 3, [1, 3]])
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, True)

    def test_with_matrix(self):
        self.assertRaises(TypeError, max_integer, [[]])
        self.assertRaises(TypeError, max_integer, [[7, 9, 0]])
        self.assertRaises(TypeError, max_integer, [[], []])

    def test_with_single_values(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

        self.assertRaises(TypeError, max_integer, [None])
        self.assertRaises(TypeError, max_integer, [True, 1])
        self.assertRaises(TypeError, max_integer, ['khairat'])

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

        self.assertRaises(TypeError, max_integer, [-1.2, -5.3, -3, -4, -5.12234])
        self.assertRaises(TypeError, max_integer, [-1.2, -5.3, 4.9, -5.12234])
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

    def test_list_with_none(self):
        self.assertRaises(TypeError, max_integer, [None, None, None])
