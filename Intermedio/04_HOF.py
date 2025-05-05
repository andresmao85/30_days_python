countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
new_countries_list = map(lambda country: country.upper(), countries)
print(list(new_countries_list))

# Use map to create a new list by changing each number to its square in the numbers list
new_numbers_list = map(lambda number: number ** 2, numbers)
print(list(new_numbers_list))

# Use map to change each name to uppercase in the names list
new_names_list = map(lambda name: name.upper(), names)
print(list(new_names_list))

# Use filter to filter out countries containing 'land'.
countries_with_land = filter(lambda country: "land" in country, countries)
print(list(countries_with_land))

# Use filter to filter out countries having exactly six characters.
countries_six_chars = filter(lambda country: len(country) == 6, countries)
print(list(countries_six_chars))

# Use filter to filter out countries containing six letters and more in the country list.
countries_six_chars_or_more = filter(lambda country: len(country) >= 6, countries)
print(list(countries_six_chars_or_more))

# Use filter to filter out countries starting with an 'E'
countries_starting_with_e = filter(lambda country: country.startswith("E"), countries)
print(list(countries_starting_with_e))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
chained = reduce(lambda a, b: a + b, filter(lambda num: num % 2 == 0,map(lambda num: num + 2, numbers)))
print(chained)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return filter(lambda item: isinstance(item, str), lst)
test_list = ["A", 1, "b", 2, "C", 3]
print(list(get_string_lists(test_list)))

# Use reduce to sum all the numbers in the numbers list.
sum_of_numbers = reduce(lambda prev, next: prev + next, numbers)
print(sum_of_numbers)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def countries_as_text(lst):
    long_list = lst[:-1]
    last_element = lst[-1]
    initial_list = reduce(lambda a, b: a + ", " + b, long_list)
    text = f"{initial_list} and {last_element} are north European countries"
    return text
print(countries_as_text(countries))

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import countries
def categorize_countries(countries_list):
    return filter(lambda country: country.startswith("K"), countries_list)

print(list(categorize_countries(countries.countries_list)))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
import string

def countries_by_letter(countries_list):
    countries_dct = {}
    for letter in string.ascii_uppercase:
        count_by_letter = len(list(filter(lambda country: country.startswith(letter), countries_list)))
        countries_dct[letter] = count_by_letter
    return countries_dct
print(countries_by_letter(countries.countries_list))

# V2 GPT
from collections import Counter

def countries_by_letter_2(countries_list):
    first_letters = [country[0].upper() for country in countries_list]
    return dict(Counter(first_letters))
print(countries_by_letter_2(countries.countries_list))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries_list):
    return countries_list[0:10]
print(get_first_ten_countries(countries.countries_list))

# V2
'''
it can be expressed using a higher-order function like itertools.islice, which takes an iterable and returns the first n elements without slicing the list directly. This can be useful if you're working with large iterables or want a more functional approach.
'''
from itertools import islice
def get_first_ten_countries_2(countries_list):
    return islice(countries_list, 10)
print(list(get_first_ten_countries_2(countries.countries_list)))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries_list):
    return countries_list[-10:]
print(get_last_ten_countries(countries.countries_list))