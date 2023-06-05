# Използва

class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration

        value = self.value
        self.value += 1
        return value


cr = CustomRange(1, 10)
cr_iter1 = iter(cr)
cr_iter2 = iter(cr)

for num in cr:
    print(num)

for num in cr_iter1:
    print(num)

for num in cr_iter2:
    print(num)


# --------------------------------

class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return CustomRangeIterator(self)

class CustomRangeIterator:
    def __init__(self, custom_range_obj: CustomRange):
        self.custom_range_obj = custom_range_obj
        self.value = custom_range_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.custom_range_obj.end:
            raise StopIteration

        value = self.value
        self.value += 1
        return value


cr = CustomRange(1, 10)
cr_iter1 = iter(cr)
cr_iter2 = iter(cr)

for num in cr:
    print(f'Iter 1: {num}')

for num in cr:
    print(f'Iter 2: {num}')

for num in cr_iter1:
    print(num)

for num in cr_iter2:
    print(num)


class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self.Iterator(self)

    class Iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_range_obj.end:
                raise StopIteration

            value = self.value
            self.value += 1
            return value


cr = CustomRange(1, 10)
cr_iter1 = iter(cr)
cr_iter2 = iter(cr)

for num in cr:
    print(num)

for num in cr_iter1:
    print(num)

for num in cr_iter2:
    print(num)


class CustomRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self.Iterator(self)

    class Iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_range_obj.end:
                raise StopIteration

            value = self.value
            self.value += 1
            return value


cr = CustomRange(1, 10)

for x in cr:
    print(f'Iter1: {x}')

for x in cr:
    print(f'Iter2: {x}')


class CustomRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self.Iterator(self)

    def __reversed__(self):
        return self.ReversedIterator(self)

    class Iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value > self.custom_range_obj.end:
                raise StopIteration

            value = self.value
            self.value += 1
            return value

    class ReversedIterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = custom_range_obj.end

        def __iter__(self):
            return self

        def __next__(self):
            if self.value < self.custom_range_obj.start:
                raise StopIteration

            value = self.value
            self.value -= 1
            return value


cr = CustomRange(1, 10)

for x in cr:
    print(f'Iter: {x}')

for x in reversed(cr):
    print(f'Reversed: {x}')


class CustomRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start

    def __iter__(self):
        return self.Iterator(self, is_reversed=False)

    def __reversed__(self):
        return self.Iterator(self, is_reversed=True)

    class Iterator:
        def __init__(self, custom_range_obj, is_reversed=False):
            self.custom_range_obj = custom_range_obj
            self.is_reversed = is_reversed
            if is_reversed:
                self.value = custom_range_obj.end
            else:
                self.value = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.value < self.custom_range_obj.start \
                    or self.value > self.custom_range_obj.end:
                raise StopIteration

            value = self.value
            if self.is_reversed:
                self.value -= 1
            else:
                self.value += 1
            return value


cr = CustomRange(1, 10)

for x in cr:
    print(f'Iter: {x}')

    print(f'Reversed: {x}')
for x in reversed(cr):
