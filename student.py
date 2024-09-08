from person import Person

class Student(Person):
    def __init__(self, name: str, age: int, student_id: int):
        super().__init__(name, age)
        self.student_id = student_id
        self.scholarship = False

    def assign_scholarship(self):
        self.scholarship = True

    def __str__(self):
        return f"Студент: {self.name}, Возраст: {self.age}, ID: {self.student_id}"

    def __repr__(self):
        return f"Student({self.name}, {self.student_id})"