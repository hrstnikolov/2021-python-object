from abc import ABC, abstractmethod


# # Version with an abstract class and abstract method
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print('Bau')
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print('miau')

# Improved version with ducktyping

class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Bau")


class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Miau")

    # def __delattr__(self, item):
    #     self.attr_from_del = item


def  make_sound(animal):
    animal.make_sound()

roshlio = Dog('Roshlio')
maca = Cat('Maca')

# # virstion 1
# roshlio.make_sound()
# maca.make_sound()

# improved version
make_sound(roshlio)
make_sound(maca)

# print("\n".join(dir(maca)))
del maca.name
print("\n".join(dir(maca)))
