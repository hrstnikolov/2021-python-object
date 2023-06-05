from typing import List


class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'Title: {self.title}'


class Library:
    def __init__(self, books: List[Book]):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.books):
            raise StopIteration

        current_index = self.index
        self.index += 1
        return self.books[current_index]


def body(element):
    print(f'Next element is {element}')


iter_obj = iter(Library([Book('Georgia'), Book('Atlas'), Book('chitanka')]))
while True:
    try:
        next_element = next(iter_obj)
        body(next_element)
    except StopIteration:
        break











