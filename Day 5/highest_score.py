student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(f"Total sum of student_score is: {total_exam_score}")
sum_of_student_score = 0

for score in student_scores:
    sum_of_student_score += score
print(f"Total sum of student_score is: {sum_of_student_score}")
print("\n")
# ***---------------------------------------------------------------------***

print(f"Highest score of a student is: {max(student_scores)}")
highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score
print(f"Highest score of a student is: {highest_score}")

