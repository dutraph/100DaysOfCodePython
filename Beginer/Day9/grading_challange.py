student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO-1: Create an empty dict called student_grades

student_grades = {}

# TODO-2: Write your code below do add the grades

for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        student_grades[student] = "Fail"
    elif score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)