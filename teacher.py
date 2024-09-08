from person import Person

class Teacher(Person):
    """Класс для учителя."""
    def __init__(self, name: str, age: int, teacher_id: int):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subjects = []

    def add_subject(self, subject):
        """Добавляем предмет для преподавания"""
        self.subjects.append(subject)
        subject.set_teacher(self)

    def __str__(self):
        return f"Учитель: {self.name}, Возраст: {self.age}, ID: {self.teacher_id}"

    def __repr__(self):
        return f"Teacher({self.name}, {self.teacher_id})"
