def a():
    print(__name__)
    print('From temp')


if __name__ == "temp":
    a()

print('-----------', __name__)