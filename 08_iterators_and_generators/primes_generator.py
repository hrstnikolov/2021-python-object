from math import sqrt


def is_prime(number):
    for x in range(2, int(sqrt(number)) + 1):
        if number % x == 0:
            return False

    return True


def generate_primes(max_number):
    number = 1
    while number <= max_number:
        if is_prime(number):
            yield number
        number += 1


primes = generate_primes(100)
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
print(next(primes))
