#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io
"""Importing unittest, Square and Rectangle modules"""

class TestSquareIniheritance(unittest.TestCase):
    """Tests the square class"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Check if Square Class is a subclass of Rectangle Class"""
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareIdInitialization(unittest.TestCase):
    """Test Square Id Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_size(self):
        """Passing only heights and width"""
        s = Square(10)
        self.assertEqual(s.id, 1)

        s1 = Square(10, 5)
        self.assertEqual(s1.id, 2)

        s2 = Square(10, 4, 0, 8)
        self.assertEqual(s2.id, 8)


class TestSquareInitialization(unittest.TestCase):
    """Test Square Initialization"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_by_passing_neg_size(self):
        """Passing negative size value"""
        with self.assertRaises(ValueError):
            s1 = Square(-23)

        """Passing 0 size value"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_by_passing_neg_x_and_y(self):
        """Passing negative x value"""
        with self.assertRaises(ValueError):
            s1 = Square(23, -10)

        """Passing negative y value"""
        with self.assertRaises(ValueError):
            s1 = Square(23, 10, -34)

    def test_by_passing_all_arguments(self):
        """Passing all arguments with id"""
        s3 = Square(10, 2, 0, 12)
        self.assertEqual(s3.id, 12)

        s = Square(78)
        self.assertEqual(s.id, 1)

    def test_invalid_types(self):
        """Testing invalid width type"""
        with self.assertRaises(TypeError):
            s1 = Square("I'm here", (23, 45))

        """Testing invalid x type"""
        with self.assertRaises(TypeError):
            s3 = Square(10, "I'm here")

        """Testing invalid y type"""
        with self.assertRaises(TypeError):
            s4 = Square(10, 2, {'car': 'Tesla'})

    def test_if_None_is_passed(self):
        """Testing None size type"""
        with self.assertRaises(TypeError):
            s1 = Square(None, 2)

        """Testing None x type"""
        with self.assertRaises(TypeError):
            s3 = Square(10, None)

        """Testing None y type"""
        with self.assertRaises(TypeError):
            s4 = Square(10, 2, None)

    def test_init_with_valid_values(self):
        """Test initializing Rectangle with valid values"""
        s = Square(10, 20, 3, 5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 3)


class TestSquareArea(unittest.TestCase):
    """Tests the area of the SquareArea"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_valid_area(self):
        """Test if 1 integers are passed"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        self.assertEqual((s1.id), 1)

    def test_invalid_area(self):
        """when negative number is passed"""
        with self.assertRaises(ValueError):
            s2 = Square(-3)
            s2.area()

        with self.assertRaises(ValueError):
            s5 = Square(0, 0)
            s5.area()


class TestSquareDisplay(unittest.TestCase):
    """Handles the display of size using #"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_valid_display(self):
        """when one is passed as width and height"""
        s = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when all the arguments are passed"""
        s2 = Square(2, 2, 3, 22)
        expected_output = (
            "\n\n\n  ##\n  ##\n"
            )
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_invalid_display(self):
        """when an invalid argument is passed"""
        with self.assertRaises(TypeError):
            s3 = Square("34", 1)
            s3.display()


class TestSquare__str__(unittest.TestCase):
    """Tests the __str__ special method"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_str_valid_method(self):
        """when all valid args are passed"""
        s1 = Square(4, 6, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 6/1 - 4")

        """when y is not passed"""
        s2 = Square(5, 5)
        self.assertEqual(str(s2), "[Square] (1) 5/0 - 5")

    def test_str_invalid_method(self):
        """when size is not passed"""
        with self.assertRaises(ValueError):
            s5 = Square(0, 0, 0, 0)
            str(s5)


class TestSquareUpdatedDisplay(unittest.TestCase):
    """Test the updated display that handles x and y"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_display_with_x_y_valid(self):
        """when valid arguments are passed"""
        s1 = Square(2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        """when zero is passed to the coordinates(x & y)"""
        s4 = Square(3, 0, 0)
        expected_output = "###\n###\n###\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s4.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_display_with_x_y_invalid(self):
        """when zero is passed to all args(x & y)"""
        with self.assertRaises(ValueError):
            s5 = Square(0, 0, 0, 0)
            s5.display()


class TestSquareUpdateSize(unittest.TestCase):
    """Test the updated display that handles x and y"""
    def setUp(self):
        """Reset the id attribute to 0 for Base class"""
        Base._Base__nb_objects = 0

    def test_update_size_with_valid_args(self):
        """passing valid args to size"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")

        """when size is 1"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s1.size = 100
        self.assertEqual(str(s1), "[Square] (2) 0/0 - 100")

    def test_update_size_with_invalid_args(self):
        """passing invalid args to size"""
        with self.assertRaises(TypeError):
            s = Square("10", 20, 30, 40)
            s.size

        """when True is passed to size"""
        with self.assertRaises(TypeError):
            s = Square(True, 20, 30, 40)
            s.size

        """when None is passed to size"""
        with self.assertRaises(TypeError):
            s = Square(None, 20, 30, 40)
            s.size
