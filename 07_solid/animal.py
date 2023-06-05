# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# # animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
from typing import List


class Animal:
    sound = None

    def make_sound(self):
        return self.sound


class Cat(Animal):
    sound = 'meow'


class Dog(Animal):
    sound = 'woof-woof'

class Chicken(Animal):
    sound = 'Chic-hiki'


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
