import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_that_number_is_divisible_by_three(self):
        self.assertTrue(fizzbuzz.is_divisible_by_three(3))

    def test_that_number_is_not_divisible_by_three(self):
        self.assertFalse(fizzbuzz.is_divisible_by_three(1))

if __name__ == '__main__':
    unittest.main()
