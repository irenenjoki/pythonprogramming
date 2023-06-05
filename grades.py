# Prompt the user to input marks for four subjects
subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))
# Calculate the total marks and average
sum =subject1+subject2+subject3+subject4
print("total marks",sum)
average = sum / 4
print("average marks",average)

# Assign grade based on average marks
if average >= 70 and average <= 100:
    grade = "A"
elif average >= 60 and average <=69:
    grade ="B"
elif average >= 50 and average <=59:
    grade ="C"
elif average >= 40 and average <=49:
    grade ="D"
elif average >= 0 and average <=39:
   grade ="Fail"
else:
 print="invalid"

    # Print the grade
print("Grade:", grade)
