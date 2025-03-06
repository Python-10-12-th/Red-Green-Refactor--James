import unittest
from roman import convert_roman_numerals  # Import the function directly

class TestRoman(unittest.TestCase):
    def test_I(self):
        self.assertEqual(convert_roman_numerals("I"), 1)  # Call function correctly

if __name__ == '__main__':
    unittest.main()
