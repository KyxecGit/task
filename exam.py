from datetime import date
from exceptions import StudentNotFoundException

class Exam:
    """Класс для экзамена"""
    def __init__(self, subject, teacher, group, exam_date: date):
        self.subject = subject
        self.teacher = teacher
        self.group = group
        self.exam_date = exam_date
        self.grades = {}

    def assign_grade(self, student, grade: int):
        """Преподаватель выставляет оценку студенту"""
        if student not in self.group:
            raise StudentNotFoundException(student.name, self.group.group_name)
        self.grades[student] = grade

    def __str__(self):
        return f"Экзамен по {self.subject.name} для группы {self.group.group_name} проведён {self.exam_date}"
