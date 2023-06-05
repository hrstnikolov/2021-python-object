class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self.Iterator(self)

    class Iterator:
        def __init__(self, countdown_iterator_obj):
            self.count = countdown_iterator_obj.count
            self.value = countdown_iterator_obj.count

        def __next__(self):
            if self.value < 0:
                raise StopIteration

            current_value = self.value
            self.value -= 1

            return current_value
1

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
