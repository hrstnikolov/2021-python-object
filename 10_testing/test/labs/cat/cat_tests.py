import unittest

from labs.cat.cat import Cat


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat(name='Tom')

    def test_cat_eat__expect_size_to_increase(self):
        """Cat's size is increased after eating"""
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_eat__expect_fed_to_be_true(self):
        """Cat is fed after eating"""
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_eat__when_already_fed__expect_exception(self):
        """Cat cannot eat if already fed, raises an error"""
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep__when_not_fed__expect_exception(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_sleep__when_successful__expect_not_sleepy(self):
        """Cat is not sleepy after sleeping"""
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)
