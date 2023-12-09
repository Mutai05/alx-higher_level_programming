#!/usr/bin/python3

# tests/test_my_module.py

import unittest
from my_module import MyClass

class TestMyClass(unittest.TestCase):
    def test_my_method(self):
        obj = MyClass()
        result = obj.my_method(3, 4)
        self.assertEqual(result, 12)  # Example test case asserting the multiplication function

if __name__ == '__main__':
    unittest.main()
