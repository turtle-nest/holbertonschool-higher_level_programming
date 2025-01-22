#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for the max_integer function."""

    def test_max_integer_with_positive_numbers(self):
        """Test with a list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_with_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_with_single_element(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([42]), 42)

    def test_max_integer_with_identical_elements(self):
        """Test with a list of identical elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_integer_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_mixed_numbers(self):
        """Test with a list containing mixed positive and negative numbers"""
        self.assertEqual(max_integer([3, -1, 4, -5, 0]), 4)

    def test_max_integer_with_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_max_integer_with_large_numbers(self):
        """Test with a list containing large numbers"""
        self.assertEqual(max_integer([1000000, 2000000, 5000000]), 5000000)

if __name__ == '__main__':
    unittest.main()
