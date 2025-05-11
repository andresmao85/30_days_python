# Write a function which count number of lines and number of words in a text:
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words
import re

def lines_and_words_counter(filename):

    file_path = f"Ejercicios/Intermedio/speeches/{filename}"
    separator = filename.index("_")
    name = filename[:separator]
    words_count = 0
    
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            words_per_line = len(re.findall(r'\b\w+\b', line))
            words_count += words_per_line
        
            
        return f"Number of lines in {name.capitalize()}'s speech: {len(lines)}. Number of words: {words_count}"

print(lines_and_words_counter("obama_speech.txt"))
print(lines_and_words_counter("michelle_obama_speech.txt"))
print(lines_and_words_counter("donald_speech.txt"))
print(lines_and_words_counter("melina_trump_speech.txt"))
'''
Number of lines in Obama's speech: 66. Number of words: 2401
Number of lines in Michelle's speech: 83. Number of words: 2265
Number of lines in Donald's speech: 48. Number of words: 1280
Number of lines in Melina's speech: 33. Number of words: 1386
'''

# V2
import re
import os

def lines_and_words_counter(filename):
    file_path = os.path.join("Ejercicios", "Intermedio", "speeches", filename)
    name_part = filename.split("_speech")[0].replace("_", " ").title()

    lines_count = 0
    words_count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            lines_count += 1
            words_count += len(re.findall(r'\b\w+\b', line))

    return f"Number of lines in {name_part}'s speech: {lines_count}. Number of words: {words_count}"

print(lines_and_words_counter("obama_speech.txt"))
print(lines_and_words_counter("michelle_obama_speech.txt"))
print(lines_and_words_counter("donald_speech.txt"))
print(lines_and_words_counter("melina_trump_speech.txt"))

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
'''
# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili')]
'''
'''
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
'''

import json

def ten_most_spoken_languages(filename, size):
    # json_file = open("Ejercicios/Intermedio/data/countries_data.json", "r")
    # languages = []
    languages = {}

    with open(filename, "r", encoding="utf-8") as json_file:
        json_dct = json.load(json_file)
        # print((json_dct[0]["languages"]))
        for country in json_dct:
            for language in country["languages"]:
            # languages.append(country["languages"])
                # languages.append(language)
                if language in languages:
                    languages[language] += 1
                else:
                    languages[language] = 1
        # sorted_languages = list(sorted(languages.items(), reverse= True, key= lambda item: item[1]))
        sorted_languages = [(count, lang) for lang, count in sorted(languages.items(), key=lambda item: item[1], reverse=True)]
    
    return sorted_languages[:size]

print(ten_most_spoken_languages("Ejercicios/Intermedio/data/countries_data.json", 11))

# V2
from collections import Counter

def ten_most_spoken_languages(filename, n):
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    language_counter = Counter()
    for country in countries:
        language_counter.update(country["languages"])

    # Convert to (count, language) and return top `n`
    return [(count, lang) for lang, count in language_counter.most_common(n)]

print("\n\n***********\n\n")



'''
print(most_populated_countries(filename='./data/countries_data.json', 10))

[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]
'''
# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
'''
print(most_populated_countries(filename='./data/countries_data.json', 3))
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]
'''
def most_populated_countries(filename: str, n: int):
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    population_counter = []
    for country in countries:
        population_counter.append({"country": country["name"], "population": country["population"]})

    return sorted(population_counter, key= lambda item: item["population"], reverse= True)[:n]

print(most_populated_countries("Ejercicios/Intermedio/data/countries_data.json", 3))

# V2
import json
from typing import List, Dict

def most_populated_countries(filename: str, n: int = 10) -> List[Dict[str, int]]:
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    population_data = [{"country": country["name"], "population": country["population"]} for country in countries]

    return sorted(population_data, key=lambda item: item["population"], reverse=True)[:n]
print(most_populated_countries(filename='Ejercicios/Intermedio/data/countries_data.json', n=3))


# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def extract_email_addresses(filename):
    email_addresses = []
    with open(filename) as file:
        lines = file.readlines()
        email_addresses = [line[6:-1] for line in lines if line.startswith("From: ")]
        print("Total email addresses:", len(email_addresses))
        return email_addresses[:10]
        

print(extract_email_addresses("Ejercicios/Intermedio/data/email_exchanges_big.txt"))

# V2 with re
import re
from typing import List

def extract_email_addresses_2(filename: str) -> List[str]:
    email_addresses = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("From: "):
                match = re.search(r'[\w\.-]+@[\w\.-]+', line)
                if match:
                    email_addresses.append(match.group())

    print(f"Total email addresses found: {len(email_addresses)}")

    # Print only the first 10 as a sample, for testing
    print("First 10 email addresses:")
    for email in email_addresses[:10]:
        print(email)

    return email_addresses
extract_email_addresses_2("Ejercicios/Intermedio/data/email_exchanges_big.txt")


# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
'''
Your output should look like this
print(find_most_common_words('sample.txt', 10))
[(10, 'the'),
(8, 'be'),
(6, 'to'),
(6, 'of'),
(5, 'and'),
(4, 'a'),
(4, 'in'),
(3, 'that'),
(2, 'have'),
(2, 'I')]
'''

'''
# Your output should look like this
print(find_most_common_words('sample.txt', 5))

[(10, 'the'),
(8, 'be'),
(6, 'to'),
(6, 'of'),
(5, 'and')]
'''