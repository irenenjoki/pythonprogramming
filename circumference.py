import math

# Get radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter
diameter = 2 * radius

# Calculate circumference
circumference = 2 * math.pi * radius

# Calculate area
area = math.pi * radius ** 2

# Print the results
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Area:", area)
