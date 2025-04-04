import unittest
from src.cipher import cipher

class TestCaesarCipher(unittest.TestCase):
    def test_basic_shift(self):
        self.assertEqual(cipher("ABC", 3), "DEF")
        self.assertEqual(cipher("aNd", 3), "dQg")
        
    def test_around(self):
        self.assertEqual(cipher("XyZ", 3), "AbC")
        self.assertEqual(cipher("z", 1), "a")
    
    def test_with_non_aplha(self):
        self.assertEqual(cipher("ZEbra and", 3), "CHeud dqg")
        self.assertEqual(cipher("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(cipher("12345", 3), "12345")
        
    def test_negative_shift(self):
        self.assertEqual(cipher("DEF", -3), "ABC")
        self.assertEqual(cipher("abc", -3), "xyz")

    def test_large_shift(self):
        self.assertEqual(cipher("ABC", 29), "DEF")  # 29 % 26 = 3
        
    def test_empty_string(self):
        self.assertEqual(cipher("", 5), "")


if __name__ == "__main__":
    unittest.main()