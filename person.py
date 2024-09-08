class Person:
    """Базовый класс для людей."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    def __repr__(self):
        return f"Person({self.name}, {self.age})"
