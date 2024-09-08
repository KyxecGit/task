from exceptions import StudentNotFoundException
from student import Student

class StudentGroup:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise StudentNotFoundException(f"Студент {student.name} не найден в группе {self.group_name}")

    def assign_scholarship(self, student: Student):
        if student in self.students:
            student.assign_scholarship()
        else:
            raise StudentNotFoundException(f"Студент {student.name} не найден в группе {self.group_name}")

    def __len__(self):
        return len(self.students)

    def __contains__(self, student: Student):
        return student in self.students

    def __iter__(self):
        return iter(self.students)

    def generate_students(self):
        for student in self.students:
            yield student

    def __str__(self):
        return f"Группа {self.group_name}, Количество студентов: {len(self.students)}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.group_name!r}, {len(self.students)} students)"
