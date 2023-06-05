# def fibonacci():
#     previous = 0
#     yield previous
#
#     current = 1
#     yield current
#
#     while True:
#         next = previous + current
#         previous, current = current, next
#         yield next

def fibonacci():
    current = 0
    next = 1

    while True:
        yield current
        current, next = next, current + next


generator = fibonacci()
for i in range(15):
    print(next(generator))
