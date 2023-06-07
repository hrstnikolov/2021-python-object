import unittest
import unittest.mock

from demos.mocking.utils import my_concat


class SampleTests(unittest.TestCase):
    def test_my_concat__when_strings__expect_success(self):
        string_values = ['hello', 'there']
        expected_output = 'hellothere'
        actual_output = my_concat(string_values)
        self.assertEqual(expected_output, actual_output)

    def test_my_concat__when_ints__expect_TypeError(self):
        int_values = [3, 5]
        with self.assertRaises(TypeError) as context:
            my_concat(int_values)

    def test_my_concat__when_float__expect_TypeError(self):
        float_values = [3.0, -1.0]
        with self.assertRaises(TypeError) as context:
            my_concat(float_values)
