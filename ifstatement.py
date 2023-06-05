# Prompt the user to input three numbers
""""num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers using if statements
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest number is:", largest)"""


    # Prompt the user to input salary and years of service
salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the years of service: "))

# Calculate the bonus amount based on the years of service
if years_of_service > 10:
    bonus_percent = 0.10
elif years_of_service >= 6:
    bonus_percent = 0.08
else:
    bonus_percent = 0.05

bonus_amount = salary * bonus_percent

# Print the bonus amount
print("Bonus Amount:", bonus_amount)