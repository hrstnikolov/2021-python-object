import math
from person import Person

from employee import Employee


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."


vasileva = Teacher()
print(vasileva.sleep())
print(vasileva.teach())
print(vasileva.get_fired())
