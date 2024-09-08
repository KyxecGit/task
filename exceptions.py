class StudentNotFoundException(ValueError):
    """Исключение выбрасывается, если студент не найден в группе."""
    pass

class SubjectNotAssignedException(ValueError):
    """Исключение выбрасывается, если учитель не преподает предмет."""
    pass
