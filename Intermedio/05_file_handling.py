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
# print(most_populated_countries(filename='Ejercicios/Intermedio/data/countries_data.json', n=3))


# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def extract_email_addresses(filename):
    email_addresses = []
    with open(filename) as file:
        lines = file.readlines()
        email_addresses = [line[6:-1] for line in lines if line.startswith("From: ")]
        print("Total email addresses:", len(email_addresses))
        return email_addresses[:10]
        

# print(extract_email_addresses("Ejercicios/Intermedio/data/email_exchanges_big.txt"))

# V2 with re
import re
from typing import List, Tuple

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
# extract_email_addresses_2("Ejercicios/Intermedio/data/email_exchanges_big.txt")


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

ENGLISH_MOST_COMMON_WORDS = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']

def find_most_common_words(source: str, n: int) -> List[Tuple[str, int]]:
    file_path = f"Ejercicios/Intermedio/speeches/{source}"
    words_count = {}

    if os.path.isfile(file_path):
        with open(file_path) as file:
            lines = file.readlines()
            for word in ENGLISH_MOST_COMMON_WORDS:
                for line in lines:
                    if word in line:
                        if word in words_count:
                            words_count[word] += 1
                        else:
                            words_count[word] = 1
        return [(count, word) for word, count in sorted(words_count.items(), key= lambda item:item[1], reverse= True)][:n]
    else:
        for word in ENGLISH_MOST_COMMON_WORDS:
            matches = re.findall(rf'\b{re.escape(word)}\b', source, re.IGNORECASE)
            if matches:
                words_count[word] = len(matches)

    # Sort and return the top `n` most common words
    return [(count, word) for word, count in sorted(words_count.items(), key=lambda item: item[1], reverse=True)][:n]

# Error, cuenta mal las palabras
print(find_most_common_words("test.txt", 7))

# V2
import os
import re
from typing import List, Tuple, Union

def find_most_common_words(source: Union[str, os.PathLike], n: int) -> List[Tuple[str, int]]:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The number of words to return (n) must be a positive integer.")

    words_count = {}

    if os.path.isfile(source):
        try:
            with open(source, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{source}' does not exist.")
    else:
        content = source

    for word in ENGLISH_MOST_COMMON_WORDS:
        matches = re.findall(rf'\b{re.escape(word)}\b', content, re.IGNORECASE)
        if matches:
            words_count[word] = len(matches)

    # Sort the words by frequency in descending order and return the top `n`
    sorted_words = sorted(words_count.items(), key=lambda item: item[1], reverse=True)
    return [(count, word) for word, count in sorted_words[:n]]

# Example usage
print(find_most_common_words("Ejercicios/Intermedio/speeches/test.txt", 7))

    # Test with a string
sample_text = ("So far we have seen different Python data types. We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt). File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.")
print(find_most_common_words(sample_text, 7))

'''
Create the function, find_most_frequent_words to find: 
a) The ten most frequent words used in Obama's speech 
b) The ten most frequent words used in Michelle's speech 
c) The ten most frequent words used in Trump's speech 
d) The ten most frequent words used in Melina's speech
'''
def find_most_frequent_words(filename):
    file_path = os.path.join("Ejercicios", "Intermedio", "speeches", filename)
    
    words_count = {}
    
    with open(file_path,"r", encoding="utf-8") as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                if word in words_count:
                    words_count[word] += 1
                else:
                    words_count[word] = 1
    sorted_words = sorted(words_count.items(), key=lambda item:item[1], reverse=True)

    return [(count, word) for word, count in sorted_words[:10]]
#  Flaw: sensitive case, counts lower and upper case apart
# print("Obama:", find_most_frequent_words("obama_speech.txt"))
# print("Michelle:", find_most_frequent_words("michelle_obama_speech.txt"))
# print("Donald:", find_most_frequent_words("donald_speech.txt"))
# print("Melina", find_most_frequent_words("melina_trump_speech.txt"))

# V2 improved
def find_most_frequent_words_2(filename):
    file_path = os.path.join("Ejercicios", "Intermedio", "speeches", filename)
    
    word_counts = {}
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())  
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1
    
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return [(word, count) for word, count in sorted_words[:10]] 

print("Obama:", find_most_frequent_words_2("obama_speech.txt"))
print("Michelle:", find_most_frequent_words_2("michelle_obama_speech.txt"))
print("Donald:", find_most_frequent_words_2("donald_speech.txt"))
print("Melina", find_most_frequent_words_2("melina_trump_speech.txt"))

# V3 GPT
import os
import re
from typing import List, Tuple
from collections import Counter

def find_most_frequent_words_3(filename: str, n: int = 10) -> List[Tuple[str, int]]:
    file_path = os.path.join("Ejercicios", "Intermedio", "speeches", filename)

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)
    most_common = word_counts.most_common(n)

    return most_common

print("Obama:", find_most_frequent_words_3("obama_speech.txt"))
print("Michelle:", find_most_frequent_words_3("michelle_obama_speech.txt"))
print("Donald:", find_most_frequent_words_3("donald_speech.txt"))
print("Melina", find_most_frequent_words_3("melina_trump_speech.txt"))


# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text (clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory.
import stop_words, string
CHARS = string.punctuation
STOP_WORDS = stop_words.stop_words

# def clean_string_text(text):
#     words = re.findall(r'\b\w+\b', text)
#     return " ".join(words).lower()
    
# # print(clean_string_text("This is your day.This is your celebration.And this – the United States of America – is your country.What truly matters is not what party controls our government but that this government is controlled by the people."))

# def clean_file_text(filename):
#     file_path = os.path.join("Ejercicios", "Intermedio", "speeches", filename)

#     with open(file_path, "r", encoding="utf-8") as file:
#         text = file.read().lower()
#         words = re.findall(r'\b\w+\b', text)

#     return " ".join(words)

# print(clean_file_text("donald_speech.txt"))

def clean_text(source):
    if os.path.isfile(source):
        try:
            with open(source, "r", encoding="utf-8") as file:
                content = file.read().lower()
        except FileNotFoundError:
            raise FileNotFoundError("The file does not exist")
    else:
        content = source.lower()
    
    words = re.findall(r'\b\w+\b', content)
    return " ".join(words)

# print(clean_text("This is your day.This is your celebration.And this – the United States of America – is your country.What truly matters is not what party controls our government but that this government is controlled by the people."))

# print(clean_text("Ejercicios/Intermedio/speeches/donald_speech.txt"))


def remove_support_words(source):
    cleaned_text = clean_text(source)
    new_text = " ".join([word for word in cleaned_text.split() if word not in STOP_WORDS])
    return new_text
        
# print(remove_support_words("This is your day.This is your celebration.And this – the United States of America – is your country.What truly matters is not what party controls our government but that this government is controlled by the people."))

# print(remove_support_words("Ejercicios/Intermedio/speeches/donald_speech.txt"))

'''
Jaccard index, also known as Jaccard similarity coefficient,  treats the data objects like sets. It is defined as the size of the intersection of two sets divided by the size of the union. Let’s continue with our previous example:

def jaccard_similarity(x,y):
    """ returns the jaccard similarity between two lists """
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
    
https://www.newscatcherapi.com/blog/ultimate-guide-to-text-similarity-with-python
'''


def check_text_similarity_jaccard(source_a, source_b):
#   returns the jaccard similarity between two lists """
    text_a = remove_support_words(source_a)
    text_b = remove_support_words(source_b)

    intersection_cardinality = len(set.intersection(*[set(text_a), set(text_b)])) 
    union_cardinality = len(set.union(*[set(text_a), set(text_b)]))
    return intersection_cardinality/float(union_cardinality)
    

print(check_text_similarity_jaccard("Ejercicios/Intermedio/speeches/melina_trump_speech.txt", "Ejercicios/Intermedio/speeches/michelle_obama_speech.txt"))


# **************************************************************

# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text (clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory.
import stop_words, string
STOP_WORDS = stop_words.stop_words

def clean_text(source):
    if os.path.isfile(source):
        try:
            with open(source, "r", encoding="utf-8") as file:
                content = file.read().lower()
        except FileNotFoundError:
            raise FileNotFoundError("The file does not exist")
    else:
        content = source.lower()
    
    words = re.findall(r'\b\w+\b', content)
    return " ".join(words)

def remove_support_words(source):
    cleaned_text = clean_text(source)
    new_text = " ".join([word for word in cleaned_text.split() if word not in STOP_WORDS])
    return new_text
        
def check_text_similarity_jaccard(source_a, source_b):
    text_a = remove_support_words(source_a)
    text_b = remove_support_words(source_b)

    intersection_cardinality = len(set.intersection(*[set(text_a), set(text_b)])) # Flaw: this builds a set of characters, not words.
    # union_cardinality = len(set.union(*[set(text_a), set(text_b)])) # original
    union_cardinality = len(set.union(*[set(text_a.split()), set(text_b.split())])) 
    
    return intersection_cardinality/float(union_cardinality)
    
# V2
import os
import re
from typing import Union
import stop_words
STOP_WORDS = stop_words.stop_words


def clean_text(source: Union[str, os.PathLike]) -> str:
    if os.path.isfile(source):
        try:
            with open(source, "r", encoding="utf-8") as file:
                content = file.read().lower()
        except Exception as e:
            raise RuntimeError(f"Error reading file '{source}': {e}")
    else:
        content = source.lower()

    words = re.findall(r'\b\w+\b', content)
    return " ".join(words)


def remove_stop_words(source: Union[str, os.PathLike]) -> str:
    cleaned_text = clean_text(source)
    filtered_words = [word for word in cleaned_text.split() if word not in STOP_WORDS]
    return " ".join(filtered_words)


def check_text_similarity_jaccard(source_a: Union[str, os.PathLike], source_b: Union[str, os.PathLike]) -> float:
    text_a = remove_stop_words(source_a).split()
    text_b = remove_stop_words(source_b).split()

    set_a = set(text_a)
    set_b = set(text_b)

    intersection = set_a & set_b
    union = set_a | set_b

    if not union:
        return 0.0  # Avoid division by zero

    return len(intersection) / len(union)

print(check_text_similarity_jaccard("Ejercicios/Intermedio/speeches/melina_trump_speech.txt", "Ejercicios/Intermedio/speeches/michelle_obama_speech.txt"))


# Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_common_words("Ejercicios/Intermedio/data/romeo_and_juliet.txt", 10))

# Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript

# a)
def count_python(file_name):
    python_count = 0
    with open(file_name, "r") as file:
        for row in file.readlines():
            if "python" in row.lower():
                python_count += 1
    return python_count


# V2 GPT

import csv
def count_python(file_name: str, word_to_count:str) -> int:
    python_count = 0

    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            line_text = " ".join(row).lower()
            words = re.findall(r'\b\w+\b', line_text)
            for word in words:
                if word == word_to_count:
                    python_count += 1
    
    return python_count
print(count_python("Ejercicios/Intermedio/data/hacker_news.csv", "python"))
print(count_python("Ejercicios/Intermedio/data/hacker_news.csv", "javascript"))
print(count_python("Ejercicios/Intermedio/data/hacker_news.csv", "java"))

