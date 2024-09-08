class Ticket:
    """Класс для экзаменационного билета"""
    def __init__(self, question: str, answer: str, teacher, signed_by_dean: bool = False):
        self.question = question
        self.answer = answer
        self.teacher = teacher
        self.signed_by_dean = signed_by_dean

    def __str__(self):
        return f"Вопрос: {self.question}, Ответ: {self.answer}, Преподаватель: {self.teacher.name}, Подписан деканом: {self.signed_by_dean}"

    def __repr__(self):
        return f"Ticket({self.question!r}, {self.answer!r}, {self.teacher.name!r})"


class TicketGenerator:
    """Класс для генерации экзаменационных билетов"""
    def __init__(self, teacher):
        self.teacher = teacher

    def generate_ticket(self, question: str, answer: str, signed_by_dean: bool = False):
        """Генерирует билет с помощью yield"""
        ticket = Ticket(question, answer, self.teacher, signed_by_dean)
        yield ticket

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
