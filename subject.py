class Subject:
    def __init__(self, name: str):
        self.name = name
        self.teacher = None  

    def set_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        return f"Предмет: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"
