import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_that_number_is_divisible_by_three(self):
        self.assertTrue(fizzbuzz.is_divisible_by(3, 3))

    def test_that_number_is_not_divisible_by_three(self):
        self.assertFalse(fizzbuzz.is_divisible_by(1, 3))

    def test_that_number_is_divisible_by_five(self):
        self.assertTrue(fizzbuzz.is_divisible_by(5, 5))

    def test_that_number_is_not_divisible_by_five(self):
        self.assertFalse(fizzbuzz.is_divisible_by(1, 5))

    def test_that_number_is_divisible_by_three_and_five(self):
        self.assertTrue(fizzbuzz.is_divisible_by(15, 15))

    def test_that_number_is_not_divisible_by_three_and_five(self):
        self.assertFalse(fizzbuzz.is_divisible_by(1, 15))

    def test_says_fizz_when_divisible_by_three(self):
        self.assertEqual(fizzbuzz.says(3), 'fizz')

    def test_says_buzz_when_divisible_by_five(self):
        self.assertEqual(fizzbuzz.says(5), 'buzz')

    def test_says_fizzbuzz_when_divisible_by_three_and_five(self):
        self.assertEqual(fizzbuzz.says(15), 'fizzbuzz')

    def test_returns_number_when_not_divisible_by_three_or_five(self):
        self.assertEqual(fizzbuzz.says(7), 7)

if __name__ == '__main__':
    unittest.main()
