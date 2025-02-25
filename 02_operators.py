# Declare your age as integer variable
age = 32

# Declare your height as a float variable
height = 176.6

# Declare a variable that store a complex number
compplex_number = 2 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
triangle_base = int(input("Enter base: "))
triangle_height = int(input("Enter height: "))
area_of_triangle = 0.5 * triangle_base * triangle_height
print(f'The area of the triangle is {area_of_triangle}')

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side A: "))
side_b = int(input("Enter side B: "))
side_c = int(input("Enter side C: "))
triangle_perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {triangle_perimeter}')

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rectangle_length = int(input("Enter rectangle length: "))
rectangle_width = int(input("Enter rectangle width: "))
rectangle_area = rectangle_length * rectangle_width
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
print(f'The area of the rectangle is {rectangle_area} and the perimeter is {rectangle_perimeter}')

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
PI_VALUE = 3.14
circle_radius = int(input("Enter the circle radius: "))
circle_area = PI_VALUE * circle_radius**2
circle_circumference = 2 * PI_VALUE * circle_radius
print(f'The area of te circle is {circle_area} and the circumference is {circle_circumference}')

# Calculate the slope, x-intercept and y-intercept of y = 2x - 2


# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_1 = len("python")
len_2 = len("dragon")
print(len_1 > len_2)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
checker = "on" in "python" and "on" in "dragon"
print(checker)

# "I hope this course is not full of jargon." Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon.")

# There is no 'on' in both dragon and python
checker_2 = "on" not in "python" and "on" not in "dragon"
print(checker_2)

# Find the length of the text python and convert the value to float and convert it to string
print(float(len_1))
print(str(len_1))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
odd_number = int(input("Enter a number: "))
print("It's an even number") if odd_number % 2 == 0 else print("It's an odd number")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7)) # True

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
print(int(9.8) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
worked_hours = int(input("Number of worked hours: "))
rate_per_hour = float(input("Rate per hour: "))
payment = worked_hours * rate_per_hour
print(f'Payment: ${payment}')