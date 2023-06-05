def read_next(*iterables):
    for iterable in iterables:
        for element in iterable:
            yield element


def read_next2(*iterables):
    for iterable in iterables:
        iterator = iter(iterable)
        while True:
            try:
                # yield next(iterator)
                yield iterator.__next__()
            except StopIteration:
                break


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')

print()

for item in read_next2('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')

# # THE SAME THING
# for element in iterable:
#     yield element
#
# iterator = iter(iterable)
# while True:
#     try:
#         yield next(iterator)
#     except StopIteration:
#         break
