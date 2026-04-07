def initialize_dict(student_name, subject_grades):
    student_dict = {
        student_name: subject_grades
    }
    return student_dict
def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    student_name = input("Enter student name:\n").title()

    subjects = {}

    while True:
        entrada = input("Enter subject and grade (or 'exit' to finish):\n")
        if entrada.lower() == "exit":
            break
        subject, grade = entrada.split(",")
        subject = subject.title()
        grade = float(grade)
        subjects[subject] = grade
    student_grades[student_name] = subjects
    print(f"Student {student_name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    result = {}
    students_lower = []
    for student in student_grades:
        students_lower.append(student.lower())
    for name in keys:
        name_lower = name.lower()
        name_title = name.title()
        if name_lower in students_lower:
            for student in student_grades:
                if student.lower() == name_lower:
                    result[student] = student_grades[student]
        else:
            print(f"{name_title} not found!")
    return result

