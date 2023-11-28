#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Testing a regular list of integers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_reversed_list(self):
        """Testing a reversed list of integers."""
        result = max_integer([4, 3, 2, 1])
        self.assertEqual(result, 4)

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()
