from student import StudentGroup
from teacher import Teacher
from subject import Subject
from exam import Exam
from ticket import TicketGenerator
from utils import generate_fake_students, generate_fake_questions
from datetime import date

# Генерация студентов и создание группы
students = generate_fake_students(10)
group = StudentGroup("Группа 228")
for student in students:
    group.add_student(student)

# Создание преподавателя и добавление предмета
subject = Subject("Математика")
teacher = Teacher(name="Александр Сергеевич", age=28, teacher_id=228)
teacher.add_subject(subject)

# Экзамен
exam = Exam(subject=subject, teacher=teacher, group=group, exam_date=date.today())
print(f"Экзамен по {subject.name} прошел {exam.exam_date}.")

# Генерация билетов
ticket_gen = TicketGenerator(teacher=teacher)
for question, answer in generate_fake_questions(5):
    ticket = next(ticket_gen.generate_ticket(question, answer))
    print(ticket)


