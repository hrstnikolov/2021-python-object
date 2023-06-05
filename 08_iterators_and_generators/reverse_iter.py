class reverse_iter:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < -len(self.iterable_obj):
            raise StopIteration

        value = self.iterable_obj[self.current_index]
        self.current_index -= 1
        return value

        # try:
        #     value = self.iterable_obj[self.current_index]
        #     self.current_index -= 1
        #     return value
        #
        # except IndexError:
        #     raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
