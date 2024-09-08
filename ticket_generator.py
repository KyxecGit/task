from ticket import Ticket

class TicketGenerator:
    def __init__(self, teacher):
        self.teacher = teacher
        self.questions_and_answers = []
        self.current_index = 0

    def add_questions(self, questions_and_answers):
        self.questions_and_answers = questions_and_answers
        self.current_index = 0 

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.questions_and_answers):
            raise StopIteration
        question, answer = self.questions_and_answers[self.current_index]
        self.current_index += 1
        return Ticket(question, answer, self.teacher)
