from person import Person
from exceptions import StudentNotFoundException

class Student(Person):
    """Класс, представляющий студента."""
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        self.student_id = student_id
        self.scholarship = False  

    def assign_scholarship(self):
        """Назначение стипендии студенту"""
        self.scholarship = True

    def __str__(self):
        return f"Студент: {self.name}, Возраст: {self.age}, ID: {self.student_id}"

    def __repr__(self):
        return f"Student({self.name}, {self.student_id})"


class StudentGroup:
    """Класс для управления группой студентов."""
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.students = []

    def add_student(self, student: Student):
        """Добавляем студента в группу"""
        self.students.append(student)

    def remove_student(self, student: Student):
        """Отчисляем студента"""
        if student in self.students:
            self.students.remove(student)
        else:
            raise StudentNotFoundException(student.name, self.group_name)

    def assign_scholarship(self, student: Student):
        """Назначаем стипендию студенту"""
        if student in self.students:
            student.assign_scholarship()
        else:
            raise StudentNotFoundException(student.name, self.group_name)

    def __len__(self):
        """Возвращаем количество студентов в группе"""
        return len(self.students)

    def __contains__(self, student: Student):
        """Проверяем, находится ли студент в группе"""
        return student in self.students

    def __iter__(self):
        """Делаем класс итерируемым"""
        return iter(self.students)

    def __str__(self):
        """Возвращаем строковое представление группы студентов"""
        return f"Группа {self.group_name}, Количество студентов: {len(self.students)}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.group_name!r}, {len(self.students)} students)"
