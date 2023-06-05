class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    @classmethod
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    @staticmethod
    def __validate_age(age):
        if age < 1:
            raise ValueError("Age must be positive number")
        else:
            return True

    def say_hello(self):
        print(f'I am {self.name}')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if self.__validate_age(value):
            self.__age = value


class Student(Person):
    def __init__(self, name, age, grade):
        # before py 3.5
        # super(Student, self).__init__(name, age)

        # after py 3.5
        super().__init__(name, age)

        self.grade = grade

    def get_student_info(self):
        print(f'studen age is {self.age}')

    @staticmethod
    def __validate_age(age):
        if age < 7:
            raise ValueError("Student must be over 7")
        else:
            return True

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if self.__validate_age(value):
            self.__age = value


chovek = Person('Ana', 3)
gosho = Student('Georgi', 122, 5)
# pesho = Student('Petar', -23, 's')
gosho.get_student_info()
gosho.say_hello()
