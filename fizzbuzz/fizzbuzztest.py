# Coding Dojo template
# Test framework
import unittest

# Code
# write your code here

def countFizz(n):
    return n // 3
    
# Tests
# Run tests by pressing arrow (run tests) on the left
class FizzBuzzTest(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(True, True)
    def test_fail(self):
        self.assertEqual(False, False)
    def test_countFizz_0_is_zero(self):
        self.assertEqual(countFizz(0),0)
    def test_countFizz_1_is_zero(self):
        self.assertEqual(countFizz(3),1)
    def test_countFizz_5_is_one(self):
        self.assertEqual(countFizz(5),1)
    def test_countFizz_6_is_two(self):
        self.assertEqual(countFizz(6),2)
    def test_countFizz_7_is_two(self):
        self.assertEqual(countFizz(7),2)
   