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
    initial_list = reduce(lambda a, b: a + ", " + b, lst[:-1])
    last_element = lst[-1]
    text = f"{initial_list} and {last_element} are north European countries"
    return text
print(countries_as_text(countries))

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.