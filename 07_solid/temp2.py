from pprint import pprint

def a():
    print(__name__)
    print('From temp')


if __name__ == "__main__":
    a()

print('23')
print(__name__)
temp.a()