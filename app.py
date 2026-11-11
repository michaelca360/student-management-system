students = []

def add_student(name, matric):
    student = {
        "name": name,
        "matric": matric
    }

    students.append(student)
    print("Student registered successfully")

def display_students():
    for student in students:
        print(student)

add_student("Mary", "2026/CSC/002")
display_students()