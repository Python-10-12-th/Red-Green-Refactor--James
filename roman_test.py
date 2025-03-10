import unittest
from roman import convert_roman_numerals 

class TestRoman(unittest.TestCase):
    def test_I(self):
        self.assertEqual(convert_roman_numerals("I"), 1)  
    def test_II(self):
        self.assertEqual(convert_roman_numerals("II"), 2) 
    def test_V(self):
        self.assertEqual(convert_roman_numerals("V"), 5)
    def test_IV(self):
        self.assertEqual(convert_roman_numerals("IV"), 4)
    def test_X(self):
        self.assertEqual(convert_roman_numerals("X"),  10)
    def test_IX(self):
        self.assertEqual(convert_roman_numerals("IX"),  9)
    def test_L(self):
        self.assertEqual(convert_roman_numerals("L"),  50)
    def test_C(self):
          self.assertEqual(convert_roman_numerals("C"),  100)
   



        
        
if __name__ == '__main__':
    unittest.main()
