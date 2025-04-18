'''
Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
'''

first_name = "Micah"
last_name = "Owens"
full_name = "Micah Owens"
country = "Belgium"
city = "Brussels"
age = 34
year = 2025
is_married = False
is_true = True
is_light_on = False
category, sub_category = "Programming", "Python"


'''
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
'''
from math import pi as PI_VALUE

print(type(first_name))
print(type(year))
print(type(is_married))
print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
print(f"The total is {total}, the difference is {diff}, the product is {product} and the division is {division}")
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(f'The remainder is {remainder}, the exponential is {exp} and the floor division is {floor_division}')
radius = 30
area_of_circle = PI_VALUE * (radius**2)
circumference = 2 * radius * PI_VALUE
print(f"The area of the circle is {area_of_circle} and the circumference is {circumference}")
radius_input = int(input("Enter the radius: "))
area_of_circle = PI_VALUE * (radius_input ** 2)
print(f"Area of your circle is {area_of_circle}")