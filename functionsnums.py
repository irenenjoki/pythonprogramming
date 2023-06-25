# Define a function to get the even numbers from a list
def get_even_numbers(numbers):
    even_numbers = []  # Create an empty list to store even numbers
    for number in numbers:  # Iterate over each number in the input list
        if number % 2 == 0:  # Check if the number is even
            even_numbers.append(number)  # If even, add it to the even_numbers list
    return even_numbers  # Return the list of even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Create a list of numbers
even_numbers = get_even_numbers(numbers)  # Call the function to get even numbers
print(even_numbers)  # Print the list of even numbers
