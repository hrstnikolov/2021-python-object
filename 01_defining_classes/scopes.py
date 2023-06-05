# scopes.py

# Scope A
a = 1  # global namespace == {a: 1}
b = 16 # global namespace == {a: 1, b:16}


def outer():
    # Scope B == част в кода
    c = 24 # local namespace за outer фунцкията == {c: 24}
    d = 'Hello, World!' # local namespace за outer фунцкията == {c: 24, d: '..'}

    def inner():
        # Scope C
        e = 'I like' # local namespace за inner фунцкията == {e: '...'}
        f = 'fried chicken'


# (Implicit) Scope D
print('Hello!')