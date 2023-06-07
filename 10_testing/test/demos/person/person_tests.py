import unittest

from demos.person.person import Person


class PersonTests(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Tom', 'Waits', 68)

    def test_get_full_name(self):
        expected_result = 'Tom Waits'
        actual_result = self.person.get_full_name()
        self.assertEqual(expected_result, actual_result)

    def test_get_info(self):
        expected_result = 'Tom Waits is 68 years old'
        actual_result = self.person.get_info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
