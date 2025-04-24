# Iterate 0 to 10 using for loop, do the same using while loop.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

count = 0
while count <= 10:
    print(count)
    count += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
numbers.reverse()
for number in numbers:
    print(number)

count = 10
while count >= 0:
    print(count)
    count -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######

x = 0
while x <= 7:
    print("#" * x) 
    x += 1

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

# V1
x = 0
y = 1
while x <= 7:
    while y <= 8:
        print("# " * 8)
        y +=1
    x += 1

# V2
rows = 8
cols = 8
for i in range(rows):
    for j in range(cols):
        print("#", end=" ")
    print()


# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

x = 0
while x <= 10:
    print(f"{x} x {x} = {x * x}")
    x += 1

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
for language in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(language)

# Use for loop to iterate from 0 to 100 and print only even numbers
for even_number in range(100):
    if even_number % 2 == 0:
        print(even_number)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for even_number in range(100):
    if even_number % 2 != 0:
        print(even_number)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for number in range(101):
    sum += number
print(f"The sum of all numbers is {sum}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_of_evens = 0
sum_of_odds = 0
for number in range(101):
    if number % 2 == 0:
        sum_of_evens += number
    else:
        sum_of_odds += number
print(f"The sum of all evens is {sum_of_evens}. And the sum of all odds is {sum_of_odds}.")

#  reverse the order using loop.
# this method modifies the original lists as it deletes the elements on it
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_list = []
while len(fruits) > 0:
    fruit = fruits.pop()
    reversed_list.append(fruit)
print(reversed_list)

# this method does not modify the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_list_2 = []
for fruit in reversed(fruits):
    reversed_list_2.append(fruit)
print(reversed_list_2)

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import countries
countries_with_land = []
for country in countries.countries_list:
    if "land" in country:
        countries_with_land.append(country)
print(f"Countries that contain \"land\": {countries_with_land}")

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# duplicated values
number_of_languages = 0
for country in countries.countries_data:
    number_of_languages += len(country["languages"])
print(f"- Number of total languages: {number_of_languages}")

# unique values
total_languages = []
for country in countries.countries_data:
    total_languages.extend(country["languages"])
unique_languages = set(total_languages)
print(f"- Number of unique languages: {len(unique_languages)}")

# >>>>>>>>>>>>>>>>> Find the ten most spoken languages from the data
spoken_lang = {}
for lang in unique_languages:
    spoken_lang[lang] = total_languages.count(lang)

sorted_lang = sorted(spoken_lang.items(), key=lambda kv: kv[1], reverse=True) # creates a list of tuples
# print(sorted_lang[0:10])
ten_more_spoken = sorted_lang[0:10]
final_list = []
for couple in ten_more_spoken:
    final_list.append(couple[0])
# print(final_list)
print("The ten most spoken languages are: ", end="")
for j in (final_list):
        print(j, end=", ")

print("\nOnly loop version\nTop 10 most spoken languages:")
# >>>>>>>>>>>>>>>>>> Only loop version
# Step 1: Count the occurrences of each language
language_counts = {}

for country in countries.countries_data:
    for language in country["languages"]:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

# Step 2: Sort languages by frequency (without using sorted())
sorted_languages = []
for lang, count in language_counts.items():
    inserted = False
    for i in range(len(sorted_languages)):
        if count > sorted_languages[i][1]:  # Insert in descending order
            sorted_languages.insert(i, (lang, count))
            inserted = True
            break
    if not inserted:
        sorted_languages.append((lang, count))

# Step 3: Get the top 10 most spoken languages
top_10_languages = sorted_languages[:10]

# Step 4: Print the result
for lang, count in top_10_languages:
    print(f"{lang}: {count}")
# >>>>>>>>>>>>>>>>>>>>>>

# Find the 10 most populated countries in the world
population_counts = {}
for country in countries.countries_data:
    population_counts[country["name"]] = country["population"]

sorted_population = []
for country, population_number in population_counts.items():
    inserted = False
    for j in range(len(sorted_population)):
        if population_number > sorted_population[j][1]:
            sorted_population.insert(j, (country, population_number))
            inserted = True
            break
    if not inserted:
        sorted_population.append((country, population_number))

top_10_populated = sorted_population[:10]
print("10 most populated countries in the world:")
for country, population_number in top_10_populated:
    print(f"{country}: {population_number:,}")