from unittest import TestCase
import unittest


def my_sum(*args):
    return sum(*args)


class SampleTests(TestCase):
    def setUp(self):
        print('Do something before each test...')

    @classmethod
    def setUpClass(cls):
        print('Do for ALL tests...')
    
    def test_my_sum__when_numbers__expect_to_be_equal(self):
        numbers = [1, 2, 3, 4]
        expected_result = sum(numbers)
        actual_result = my_sum(numbers)

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_mixed__expect_typeerror(self):
        mixed = [1, 2, 3, "a"]
        self.assertRaises(TypeError, my_sum, mixed)


if __name__ == '__main__':
    unittest.main()