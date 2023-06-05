class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @classmethod
    def from_str(cls, s):
        args = s.split(', ')
        return cls(*args)

    def __repr__(self):
        return self.__dict__.__str__()

    def __setattr__(self, key, value):
        if key.startswith('_'):
            key = f'_{self.__class__.__name__}${key[1:]}'

        return super().__setattr__(key, value)


ivan = Person.from_str('ivan, 25')
print(ivan)