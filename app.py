students = []

def add_student(name, matric):
    student = {
        "name": name,
        "matric": matric
    }
    students.append(student)

def display_students():
    for student in students:
        print(student)

add_student("John", "2026/CSC/001")
display_students()