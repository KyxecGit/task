from student_group import StudentGroup
from teacher import Teacher
from subject import Subject
from exam import Exam
from ticket_generator import TicketGenerator
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

# Использование генератора для вывода студентов
print("Список студентов:")
for student in group.generate_students():
    print(f"Студент: {student.name}, ID: {student.student_id}")

# Вывод информации о студентах и их оценках
print(f"\nЭкзамен по {subject.name} прошел {exam.exam_date}.")

# Генерация билетов
ticket_gen = TicketGenerator(teacher=teacher)
questions_and_answers = generate_fake_questions(5)
ticket_gen.add_questions(questions_and_answers)

while True:
    try:
        ticket = next(ticket_gen)  
        print(ticket)
    except StopIteration:
        break
