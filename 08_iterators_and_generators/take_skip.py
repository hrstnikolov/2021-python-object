# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#         self.current_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index >= self.count:
#             raise StopIteration
#
#         current_index = self.current_index
#         self.current_index += 1
#
#         return current_index * self.step


# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#
#     def __iter__(self):
#         self.current_index = 0
#         return self
#
#     def __next__(self):
#         if self.current_index >= self.count:
#             raise StopIteration
#
#         current_index = self.current_index
#         self.current_index += 1
#
#         return current_index * self.step

# class take_skip:
#     def __init__(self, step, count):
#         self.step = step
#         self.count = count
#
#     def __iter__(self):
#         return self.generator_function()
#
#     def generator_function(self):
#         for number in range(self.count):
#             yield number * self.step

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count

    def __iter__(self):
        return (n * self.step for n in range(self.count))



numbers = take_skip(2, 6)
# print(type(numbers.__iter__()))
# print(type(numbers.__iter__))
for number in numbers:
    print(number)

