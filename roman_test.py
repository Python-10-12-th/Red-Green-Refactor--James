import unittest
from roman import convert_roman_numerals 

class TestRoman(unittest.TestCase):
    def test_I(self):
        self.assertEqual(convert_roman_numerals("I"), 1)  
    def test_II(self):
        self.assertEqual(convert_roman_numerals("II"), 2) 
if __name__ == '__main__':
    unittest.main()
