import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_that_number_is_divisible_by_three(self):
        self.assertTrue(fizzbuzz.is_divisible_by_three(3))

if __name__ == '__main__':
    unittest.main()
