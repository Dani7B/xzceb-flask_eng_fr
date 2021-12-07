import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(englishToFrench(None)) # test when is given null input
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  # test when Hello is given as input the output is Bonjour.        

class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertIsNone(frenchToEnglish(None)) # test when is given null input
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test when Bonjour is given as input the output is Hello.        

unittest.main()