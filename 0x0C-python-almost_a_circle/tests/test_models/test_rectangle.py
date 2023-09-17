#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
import io
"""Importing unittest, Base and Rectangle modules"""


class TestRectangle(unittest.TestCase):
    """Tests the rectangle class"""
    @classmethod
    def setUpClass(cls):
        """Reset the __nb_objects counter to 0 before running
        any test methods in this class."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Check if Rectangle Class is a subclass of Base Class"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_by_passing_hight_and_width(self):
        """Passing only heights and width"""
        r = Rectangle(10, 78)
        self.assertEqual(r.id, 2)

        r1 = Rectangle(10, 5)
        self.assertEqual(r1.id, 3)

        r2 = Rectangle(10, 4, 8, 0, 8)
        self.assertEqual(r2.id, 8)

        r3 = Rectangle(10, 4)
        self.assertEqual(r3.id, 4)

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

        rec = Rectangle(78, 70)
        self.assertEqual(rec.id, 1)

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

    def test_valid_area(self):
        """Test if 2 integers are passed"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        self.assertEqual((r1.id), 36)

        """when argumnets are passed"""
        r4 = Rectangle(10, 100, 0, 0, 12)
        self.assertEqual(r4.area(), 1000)

    def test_invalid_area(self):
        """when neative number is passed to width"""
        with self.assertRaises(ValueError):
            r2 = Rectangle(-3, 2)
            r2.area()

        """when negative number is passed to heigth"""
        with self.assertRaises(ValueError):
            r3 = Rectangle(6, -3)
            r3.area()

        with self.assertRaises(ValueError):
            r4 = Rectangle(6, 0)
            r3.area()

    def test_valid_display(self):
        """when one is passed as width and height"""
        rec = Rectangle(4, 2)
        expected_output = "####\n####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rec.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when 2 valid arguments are passed"""
        r2 = Rectangle(1, 1)
        expected_output = "#\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when all the arguments are passed"""
        r2 = Rectangle(10, 5, 2, 3, 22)
        expected_output = (
            "\n\n\n  ##########\n  ##########\n  ##########\n  ##########\n"
            "  ##########\n"
        )
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """Display a Square"""
        r2 = Rectangle(4, 4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_invalid_display(self):
        """when an invalid argument is passed"""
        with self.assertRaises(TypeError):
            r3 = Rectangle("34", 1)
            r3.display()

        """when an invalid argument is passed to height"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(2, (56, 99))
            r4.display()

        """when 0 is passed as both arguments"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0)
            r5.display()

        """when 0 is passed as one argument"""
        with self.assertRaises(ValueError):
            r6 = Rectangle(0, 8)
            r6.display()

    def test_str_valid_method(self):
        """when all valid args are passed"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        """when y is not passed"""
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (28) 1/0 - 5/5")

        """when x is not passed"""
        r3 = Rectangle(5, 5, y=1)
        self.assertEqual(str(r3), "[Rectangle] (29) 0/1 - 5/5")

        """when height is not passed"""
        r4 = Rectangle(5, 7)
        self.assertEqual(str(r4), "[Rectangle] (30) 0/0 - 5/7")

    def test_str_invalid_method(self):
        """when width is not passed"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0, 0, 0, 0)
            str(r5)

    def test_update_display_with_x_y_valid(self):
        """when valid arguments are passed"""
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to one of the coordinates(y)"""
        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to one of the coordinates(x)"""
        r3 = Rectangle(3, 2, 0, 1)
        expected_output = "\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r3.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to the coordinates(x & y)"""
        r4 = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_display_with_x_y_invalid(self):
        """when zero is passed to all args(x & y)"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0, 0, 0)
            r5.display()
