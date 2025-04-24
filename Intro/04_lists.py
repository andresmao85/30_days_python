from math import ceil

# Declare an empty list
my_list = []

# Declare a list with more than 5 items
my_new_list = ["a", "b", "c", "d", "e", "f", "g"]
print(type(my_new_list))

# Find the length of your list
print(len(my_new_list))

# Get the first item, the middle item and the last item of the list
print(my_new_list[0])
print(my_new_list[-1])
# first_item = my_new_list[0]
last_item = len(my_new_list) - 1
middle_item = int(last_item / 2)
print(my_new_list[middle_item])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Mauro", 39, 1.77, "married", "Cra 11 9-79"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(f"Number of companies: {len(it_companies)}")

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
last_company = len(it_companies) - 1 
middle_company = int(last_company / 2)
print(it_companies[middle_company])

# Print the list after modifying one of the companies
it_companies[3] = "Linkedin"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("SophiLabs")

# Insert an IT company in the middle of the companies list
it_companies.insert(middle_company, "Nvidia")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list.
print("Amazon" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[0:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[middle_company])

# Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.remove(it_companies[middle_company])

# Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

'''
Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
redux_index = int(full_stack.index("Redux"))
full_stack.insert(redux_index + 1, "SQL")
full_stack.insert(redux_index + 1, "Python")
print(full_stack)

'''
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.insert(0, min_age)
ages.append(max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
middle_age = int((len(ages) - 1) / 2)
median_age = int(ages[middle_age] / 2)
print(median_age)

# Find the average age (sum of all items divided by their number )
number_of_ages = len(ages)
sum_of_ages = sum(age for age in ages)
average_age = sum_of_ages/number_of_ages
print(f"The average age is {average_age}")

# Find the range of the ages (max minus min)
range_of_ages = max_age - min_age
print(f"Range: {range_of_ages}")

# Compare the value of (min - average) and (max - average), use abs() method
comparison = abs(min_age - average_age) >= (max_age - average_age)
print(comparison)

# Find the middle country(ies) in the countries list
countries = [
'Afghanistan',
'Albania',
'Algeria',
'Andorra',
'Angola',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bhutan',
'Bolivia',
'Bosnia and Herzegovina',
'Botswana',
'Brazil',
'Brunei',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cambodia',
'Cameroon',
'Canada',
'Cape Verde',
'Central African Republic',
'Chad',
'Chile',
'China',
'Colombi',
'Comoros',
'Congo (Brazzaville)',
'Congo',
'Costa Rica',
"Cote d'Ivoire",
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'East Timor (Timor Timur)',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Ethiopia',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia, The',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Honduras',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Israel',
'Italy',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea, North',
'Korea, South',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macedonia',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russia',
'Rwanda',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Vincent',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia and Montenegro',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syria',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'Togo',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Zimbabwe',
]

# Find the middle country(ies) in the countries list
last_country_index = len(countries) - 1
first_list_length = ceil(len(countries) / 2) if len(countries) %2 != 0 else int(len(countries) / 2)
print(f"Middle country: {countries[first_list_length]}")

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(f"Total countries number: {len(countries)}") # 193 countries
first_countries_list = countries[0:first_list_length]
second_countries_list = countries[first_list_length:]
print(f"First list length: {len(first_countries_list)}")
print(f"Second list length: {len(second_countries_list)}")

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = countries
print(f"Other countries: {ch}, {ru}, {us}. Scandic countries: {scandic}")
