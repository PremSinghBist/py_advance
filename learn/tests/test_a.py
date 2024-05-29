from src.a import sum
import unittest
class Test_testSum(unittest.TestCase):
    def test_sum(self):
        result  = sum(2, 5)
        print("Test run successfully")
        self.assertEqual(result, 7)
        
    def test_sum_failed(self):
        result  = sum(2, 6)
        print("Test run successfully")
        self.assertEqual(result, 7)
        
        