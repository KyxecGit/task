from faker import Faker
from student import Student

fake = Faker('ru_Ru')

def generate_fake_students(num_students: int):
    """Создание списка студентов с фейковыми данными"""
    return [Student(name=fake.name(), age=fake.random_int(min=18, max=25), student_id=fake.random_int(min=1000, max=9999)) for _ in range(num_students)]

def generate_fake_questions(num_questions: int):
    """Создание списка вопросов для экзамена"""
    return [(fake.sentence(), fake.sentence()) for _ in range(num_questions)]
