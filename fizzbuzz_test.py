import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_that_number_is_divisible_by_three(self):
        self.assertTrue(fizzbuzz.is_divisible_by_three(3))

    def test_that_number_is_not_divisible_by_three(self):
        self.assertFalse(fizzbuzz.is_divisible_by_three(1))

    def test_that_number_is_divisible_by_five(self):
        self.assertTrue(fizzbuzz.is_divisible_by_five(5))

    def test_that_number_is_not_divisible_by_five(self):
        self.assertFalse(fizzbuzz.is_divisible_by_five(1))

    def test_that_number_is_divisible_by_three_and_five(self):
        self.assertTrue(fizzbuzz.is_divisible_by_three_and_five(15))

    def test_that_number_is_not_divisible_by_three_and_five(self):
        self.assertFalse(fizzbuzz.is_divisible_by_three_and_five(1))

if __name__ == '__main__':
    unittest.main()
