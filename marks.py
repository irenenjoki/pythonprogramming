num_of_subjects = int(input("Enter the number of subjects: "))

# Initialize variables
marks = []
total_marks = 0

# Get marks for each subject from the user
for i in range(num_of_subjects):
    subject_mark = float(input("Enter the marks for subject {}: ".format(i + 1)))
    marks.append(subject_mark)
    total_marks += subject_mark

# Calculate the sum and average
sum_marks = total_marks
average_marks = sum_marks / num_of_subjects

# Determine the grade based on average marks
grade = ""
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 50:
    grade = "D"
else:
    grade = "F"

# Output the results
print("Sum of marks:", sum_marks)
print("Average marks:", average_marks)
print("Grade:", grade)
