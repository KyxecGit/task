class StudentNotFoundException(Exception):
    """Исключение выбрасывается, если студент не найден"""
    def __init__(self, student_name, group_name):
        super().__init__(f"Студент {student_name} не найден в группе {group_name}")

class SubjectNotAssignedException(Exception):
    """Исключение выбрасывается, если учитель не преподает предмет"""
    def __init__(self, teacher_name, subject_name):
        super().__init__(f"Учитель {teacher_name} не преподает предмет {subject_name}")
