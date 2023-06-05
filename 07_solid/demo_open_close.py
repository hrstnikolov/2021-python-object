class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class StudentTaxes:
    def __init__(self, student, semester_tax):
        self.student = student
        self.semester_tax = semester_tax

    def get_student_discount(self):
        return 0


class ExcellentStudentTaxes(StudentTaxes):
    def get_student_discount(self):
        if self.student.grade >= 5:
            return 0.4 * self.semester_tax
        return super().get_student_discount()


class GoodStudentTaxes(StudentTaxes):
    def get_student_discount(self):
        if self.student.grade >= 4:
            return 0.2 * self.semester_tax
        return super().get_student_discount()


s1 = Student('Pesho', 32)
tax1 = StudentTaxes(s1, 750)
