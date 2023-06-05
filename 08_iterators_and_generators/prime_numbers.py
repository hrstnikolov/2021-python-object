from math import sqrt


def is_prime(number):
    if number in (0, 1):
        return False

    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False

    return True


def get_primes(integer_list):
    for number in integer_list:
        if is_prime(number):
            yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
