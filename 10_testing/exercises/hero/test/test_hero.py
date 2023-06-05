from unittest import TestCase

from project.hero import Hero


class TestHero(TestCase):
    def test_battle__when_same_username__expect_exception(self):
        my_hero = Hero(username='Gandalf', level=11, health=80, damage=3)
        enemy_hero = Hero(username='Gandalf', level=6, health=120, damage=4)
        with self.assertRaises(Exception) as context:
            my_hero.battle(enemy_hero)

    # def test2(self):
    #     enemy_hero = Hero(username='Voldemort', level=6, health=120, damage=4)
