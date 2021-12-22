student_list = input("Input the list of student heights: ").split()
total_height = 0

for i in range(0, len(student_list)):
    student_list[i] = int(student_list[i])
    total_height += i  # Asked to not use len() or sum()
sum_heights = 0

for student in student_list:
    sum_heights += student

rounded_avg = round(sum_heights / total_height)

print(rounded_avg)
