# METHOD 1: CLASS AND ITERATOR CLASS
# class vowels:
#     def __init__(self, text):
#         self.text = text
#
#     def __iter__(self):
#         return self.Iterator(self)
#
#     class Iterator:
#
#         def __init__(self, vowels_obj):
#             self.text = vowels_obj.text
#             self.current_index = 0
#
#         def __next__(self):
#             if self.current_index >= len(self.text):
#                 raise StopIteration
#
#             ch = self.text[self.current_index]
#             self.current_index += 1
#             if not self.is_vowel(ch):
#                 return self.__next__()
#
#             return ch
#
#         @staticmethod
#         def is_vowel(ch):
#             return ch.lower() in {'a', 'y', 'o', 'u', 'e', 'i'}


# # METHOD 2: GENERATOR FUNCTION
# def vowels(text):
#     vowels_list = {'a', 'y', 'o', 'u', 'e', 'i'}
#     for ch in text:
#         if ch.lower() in vowels_list:
#             yield ch


# METHOD 3: GENERATOR COMPREHENSION
def vowels(text):
    vowels_list = {'a', 'y', 'o', 'u', 'e', 'i'}

    return (ch for ch in text if ch.lower() in vowels_list)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(f"Iter 1:{char}")

for char in my_string:
    print(f"Iter 2:{char}")
