student_scores = input("Input the list of student heights: ").split()
highets_score = 0

for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
    if (student_scores[i] > highets_score):
        highets_score = student_scores[i]
print(student_scores)
print(f"th highest score in the class is: {highets_score}")