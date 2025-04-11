# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_1, num_2):
    return num_1 + num_2

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14 * r * r 

import math
def area_of_circle2(r):
    return math.pi * r**2

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    try:
        for num in nums:
            total += num
        return total
    except TypeError:
        print("Please use only integer values")

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_c_to_f(temperature_in_celsius):
    return (temperature_in_celsius * 9 / 5) + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
def check_season(month):
    if month.capitalize() in autumn:
        return "The season is Autumn"
    elif month.capitalize() in winter:
        return "The season is Winter"
    elif month.capitalize() in spring:
        return "The season is Spring"
    elif month.capitalize() in summer:
        return "The season is Summer"
print(check_season("july"))

# V2
def check_season2(month):
    month = month.capitalize()
    seasons = {
        "Autumn": ["September", "October", "November"],
        "Winter": ["December", "January", "February"],
        "Spring": ["March", "April", "May"],
        "Summer": ["June", "July", "August"]
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return ("Invalid month")

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    if x1 == x2:
        return "Undefined (vertical line)"
    return (y2 - y1) / (x2 -x1)

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

'''         ____________
 x = -b +- V b**2 - 4ac
     ------------------
             2a
'''

def solve_quadratic_eqn(a, b, c):
    discriminant = b * b - 4 * a * c  # Calculate the discriminant

    if discriminant > 0:  # Only proceed if there are two real solutions
        sqrt_discriminant = discriminant ** 0.5  # Compute square root manually
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return (x1, x2)
    else:
        return "No two real solutions"

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for element in list:
        print(element)
fruits = ['banana', 'orange', 'mango', 'grape']
print_list(fruits)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reversed_list = []
    for item in reversed(array):
        reversed_list.append(item)
    return reversed_list
print(reverse_list(fruits))
print(reverse_list([1, 2, 3, 4, 5]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    capitalized_items = []
    for element in list:
        capitalized_items.append(element.capitalize())
    return capitalized_items
print(capitalize_list_items(fruits))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list, item):
    list.append(item)
    return list
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list, item):
    list.pop(item)
    return list
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    sum_of_odds = 0
    for j in range(number + 1):
        if j %2 != 0:
            sum_of_odds += j
    return sum_of_odds
print(sum_of_odds(100))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    sum_of_even = 0
    for j in range(number + 1):
        if j %2 == 0:
            sum_of_even += j
    return sum_of_even
print(sum_of_even(100))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    number_of_evens = 0
    number_of_odds = 0
    for k in range(number + 1):
        if k %2 == 0:
            number_of_evens +=1
        else:
            number_of_odds +=1
    return f"The number of odds is {number_of_odds}.\nThe number of evens is {number_of_evens}."
print(evens_and_odds(100))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    factorial_of_num = 1
    while num > 0:
        factorial_of_num *= num
        num -= 1
    return f"{factorial_of_num:,}"
print(factorial(15))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# V1
def is_empty(item):
    if item:
        return f"It is not empty"
    else:
        return f"It is empty"
empty_list = []
print(is_empty(empty_list))

# V2 >> More "Pythonic" > Python treats empty values ("", [], {}, set(), None, 0, etc.) as False, so you can return not item directly.
def is_empty2(item):
    return not item 
print(is_empty2(empty_list))
print(is_empty2(numbers))

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(list):
    sum_of_elements = 0
    for n in list:
        sum_of_elements += n
    mean = sum_of_elements / len(list)
    return mean
print(calculate_mean([7,3,5,6,9]))

def calculate_median(list):
    list = sorted(list)
    n = len(list)
    mid = n // 2

    if n % 2 == 1:
        return list[mid]
    else:
        return (list[mid - 1] + list[mid]) / 2
print(calculate_median([7, 3, 1, 4]))
print(calculate_median([7,3,5,6,9]))

def calculate_mode(list):
    frequency = {}
    for number in list:
        if number in frequency.keys():
            frequency[number] += 1
        else:
            frequency[number] = 1
    max_count = max(frequency.values())
    
    modes = [num for num, count in frequency.items() if count == max_count]

    return modes if len(modes) > 1 else modes[0]

print(calculate_mode([7, 3, 1, 4, 7, 3, 7])) #7
print(calculate_mode([7, 3, 1, 4, 7, 3, 7, 3])) #3 
print(calculate_mode([7, 3, 1, 4])) #7, 3, 1, 4

def calculate_range(list):
    return max(list) - min(list)
print(calculate_range([7, 3, 1, 4, 7, 3, 7]))

def calculate_variance(list):
    sum_of_elements = 0
    for m in list:
        sum_of_elements += m
    mean = sum_of_elements / len(list)

    sqr_deviation = 0
    for x in list:
        sqr_deviation += (x - mean)**2
    
    sample_variance = sqr_deviation / (len(list) - 1)

    return sample_variance
print("VARIANCE")
print(calculate_variance([2, 4, 4, 4, 5, 5, 7, 9]))
print(calculate_variance([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]))


def calculate_std(list):
    sum_of_elements = 0
    for y in list:
        sum_of_elements += y
    mean = sum_of_elements / len(list)

    sqr_difference = 0
    for n in list:
        sqr_difference += (n - mean) ** 2
    
    sample_variance = sqr_difference / (len(list) - 1)

    std = sample_variance ** 0.5

    return f"{std:.2f}"
print(calculate_std([2, 4, 4, 4, 5, 5, 7, 9]))



# Write a function called is_prime, which checks if a number is prime.
# V1 with issues
def is_prime(number):
    divider = 2
    prime = True
    while divider < number / 2:
        if number % divider != 0:
            divider += 1
        else:
            prime = False
            break
    return prime
print(is_prime(2))
        
# V2 corrected
def is_prime_2(num):
    if num < 2:
        return False
    
    if num == 2:
        return True

    if num % 2 == 0: 
        return False
    
    divisor = 3
    while divisor * 3 <= num:
        if num % divisor == 0:
            return False
        divisor += 2
    
    return True
print(is_prime_2(1))   # False
print(is_prime_2(2))   # True
print(is_prime_2(3))   # True
print(is_prime_2(4))   # False
print(is_prime_2(17))  # True
print(is_prime_2(19))  # True
print(is_prime_2(25))  # False

# Write a functions which checks if all items are unique in the list.
# V1
def check_unique(items_list):
    items_set = set(items_list)
    if len(items_set) == len(items_list):
        return True
    else:
        return False

# V2
def check_unique(items_list):
    return len(set(items_list)) == len(items_list)

# V3
def check_unique(items_list):
    seen = set()
    for item in items_list:
        if item in seen:
            return False
        seen.add(item)

print(check_unique(fruits))
print(check_unique([2, 4, 4, 4, 5, 5, 7, 9]))


# Write a function which checks if all the items of the list are of the same data type.
def check_type(items_list):
    for item in items_list:
        if type(item) == type(items_list[0]):
            return False
    return True
    
print(check_type(["a", 2]))

# Write a function which check if provided variable is a valid python variable

# V1
print("Check variable name:\n")
def check_variable_name(variable_name):
    if variable_name[0] == "_" and variable_name[1:].isalnum() or "_" in variable_name[1:]:
        return True
    
    if variable_name[0].isnumeric() or not variable_name[0].isalpha() or not variable_name[1:].isalnum():
        return False
    
    if variable_name.isalnum():
        return True


# V2
python_keywords = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
    'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'with', 'yield'
}

def check_variable_name(name):
    return name.isidentifier() and name not in python_keywords

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
import countries
def most_spoken_languages(countries_info):
    language_counts = {}
    
    for country in countries_info:
        for language in country["languages"]:
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1
    
    sorted_languages = []
    for lang, count in language_counts.items():
        inserted = False
        for i in range(len(sorted_languages)):
            if count > sorted_languages[i][1]:
                sorted_languages.insert(i, (lang, count))
                inserted = True
                break
        if not inserted:
            sorted_languages.append((lang, count))
    
    top_20_languages = sorted_languages[:20]

    # for lang, count in top_20_languages:
    #     print(f"{lang}: {count}")
    return sorted_languages[:20]

# most_spoken_languages(countries.countries_data)

for lang, count in most_spoken_languages(countries.countries_data):
    print(f"{lang}: {count}")


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries_info):
    population_counts = {}
    for country in countries_info:
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

    top_10_populated = sorted_population[:20]
    print("20 most populated countries in the world:")
    for country, population_number in top_10_populated:
        print(f"{country}: {population_number:,}")

most_populated_countries(countries.countries_data)