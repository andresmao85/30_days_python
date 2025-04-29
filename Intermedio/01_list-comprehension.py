# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_list = [i for i in numbers if i <= 0]
print(filtered_list)

# Flatten the following list of lists of lists to a one dimensional list :
# output [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

pre_flattened_list = [lst for row in list_of_lists for lst in row]
flattened_list = [num for lst in pre_flattened_list for num in lst]
print(flattened_list)

# V2
flattened_list = [num for sublist in list_of_lists for lst in sublist for num in lst]
print(flattened_list)

# Using list comprehension create the following list of tuples:

'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''

nums = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
# print(numbers)

# V2
nums = [(i, *[(i ** j) for j in range(6)]) for i in range(11)]

# V3
nums = [(i, *(i ** j for j in range(6))) for i in range(11)]

# V4
nums = [tuple([i] + [i ** j for j in range(6)]) for i in range(11)]
print(nums)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
'''
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
'''
flattened_countries = list(([country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries))
print(flattened_countries)

# V2
flattened_countries = [[name.upper(), name[:3].upper(), capital.upper()] for [(name, capital)] in countries]
print(flattened_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
'''
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''
countries_dct = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(countries_dct)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
'''
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
'''
# names_list = ' '.join(names[0][0])
names_list = [' '.join(name) for [(name)] in names]
print(names_list)

