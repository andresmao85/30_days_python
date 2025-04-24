# Create an empty dictionary called dog
dog = {}
print(type(dog))

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Firulais"
dog["color"] = "white"
dog["breed"] = "border collie"
dog["legs"] = 4
dog["age"] = 7
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student["first_name"] = "John"
student["last_name"] = "Doe"
student["gender"] = "Male"
student["age"] = 22
student["marital_status"] = "Single"
student["skills"] = ["Python", "Java", "C#"]
student["country"] = "Colombia"
student["city"] = "Armenia"
student["address"] = "123 Main St"
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].append("C++")
student["skills"].append("COBOL")
print(student["skills"])

# Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# Get the dictionary values as a list
student_values = student.values()
print(student_values)

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student["age"]
print(student)

# Delete one of the dictionaries
del dog