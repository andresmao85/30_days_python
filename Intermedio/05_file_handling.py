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


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
'''
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
'''

def get_countries_pop(data, size):
    pass