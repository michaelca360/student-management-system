from app import add_student, students

def test_add_student():
    students.clear()

    add_student("Mary", "2026/CSC/002")

    assert len(students) == 1
    assert students[0]["name"] == "Mary"