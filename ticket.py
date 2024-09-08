class Ticket:
    def __init__(self, question: str, answer: str, teacher, signed_by_dean: bool = False):
        self.question = question
        self.answer = answer
        self.teacher = teacher
        self.signed_by_dean = signed_by_dean

    def __str__(self):
        return f"Вопрос: {self.question}, Ответ: {self.answer}, Преподаватель: {self.teacher.name}, Подписан деканом: {self.signed_by_dean}"

    def __repr__(self):
        return f"Ticket({self.question!r}, {self.answer!r}, {self.teacher.name!r})"
