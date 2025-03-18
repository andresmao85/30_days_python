# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output: You need x more years to learn to drive.

age = int(input("Enter your age: "))
print("You are old enough to drive") if age >= 18 else print(f"You need {18 - age} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
my_age = 39
your_age = int(input("Enter your age: "))
age_difference = abs(my_age - your_age)

if age_difference == 0:
    print("We have the same age.")
elif my_age > your_age:
        print("I am 1 year older than you") if age_difference == 1 else print(f"I am {age_difference} years older than you")
else:
    print("You are 1 year older than me") if age_difference == 1 else print(f"You are {age_difference} years older than me")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
number_a = int(input("Enter number a: "))
number_b = int(input("Enter number b: "))

if number_a == number_b:
    print("a is equal to b")
else:
    print("a is greater than b") if number_a > number_b else print("b is greater than a")

# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-79, B
# 60-69, C
# 50-59, D
# 0-49, F

grade = int(input("Enter score: "))
if grade >= 80:
    print("A")
elif 69 < grade < 80:
    print("B")
elif 59 < grade < 70:
    print("C")
elif 49 < grade < 60:
    print("D")
elif grade <= 49:
    print("F")

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: 
# September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
month = input("Enter month: ")
if month in autumn:
    print("The season is Autumn")
elif month in winter:
    print("The season is Winter")
elif month in spring:
    print("The season is Spring")
elif month in summer:
    print("The season is Summer")

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')'
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Fruit name: ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person.keys():
    skills_number = len(person['skills'])
    middle_skill = int(skills_number / 2)
    print(person['skills'][middle_skill])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person.keys():
    if "Python" in person["skills"]:
        print("Skill found: Python")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if len(person['skills']) > 3 and ('JavaScript' and 'React' and 'Node' and 'MongoDB' and 'Python' in person['skills']):
    print("He is a fullstack developer")
elif len(person['skills']) == 2 and ('JavaScript' and 'React' in person['skills']):
    print("He is a frontend developer")
elif len(person['skills']) == 3 and ('Node' and 'MongoDB' and 'Python' in person['skills']):
    print("He is a backend developer")
else:
    print("Unknown title")

# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and person['country'] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")