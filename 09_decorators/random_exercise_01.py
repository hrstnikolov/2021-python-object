# 09 DECORATORS

def get_current_temp():
    return '23 degC'


def uppercase(func):
    return func.upper()

def uppercase2(func):
    result = func()
    return result

print(get_current_temp())
print(uppercase(get_current_temp()))

