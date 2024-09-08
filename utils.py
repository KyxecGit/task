from faker import Faker
from student import Student

fake = Faker()

MIN_AGE = 18
MAX_AGE = 25
MIN_STUDENT_ID = 1000
MAX_STUDENT_ID = 9999

def generate_fake_students(num_students: int):
    return [Student(name=fake.name(), age=fake.random_int(min=MIN_AGE, max=MAX_AGE), student_id=fake.random_int(min=MIN_STUDENT_ID, max=MAX_STUDENT_ID)) for _ in range(num_students)]

def generate_fake_questions(num_questions: int):
    return [(fake.sentence(), fake.sentence()) for _ in range(num_questions)]
