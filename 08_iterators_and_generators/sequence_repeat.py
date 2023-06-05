# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = sequence
#         self.number = number
#         self.current_number = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_number >= self.number:
#             raise StopIteration
#
#         index = self.current_number % len(self.sequence)
#         self.current_number += 1
#
#         return self.sequence[index]

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_number = 0

    def __iter__(self):
        self.current_number = 0
        return self

    def __next__(self):
        if self.current_number >= self.number:
            raise StopIteration

        index = self.current_number % len(self.sequence)
        self.current_number += 1

        return self.sequence[index]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

for item in result:
    print(item, end='')
