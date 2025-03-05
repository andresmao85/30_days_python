it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Nvidia", "Compaq", "SophiLabs"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Facebook")
print(it_companies)

# What is the difference between remove and discard > does not yield an error if element is not present.
# Remove is used if the item is expected to be in the set and show an error if it isn't
# Discard is used if the item is not expected to be and an error is not wanted if it isn't in the set
it_companies.discard("Facebook")
print(it_companies)

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
intersection_AB = A.intersection(B)
print(intersection_AB)

# Is A subset of B
print(A.issubset(B))    

# Are A and B disjoint sets
print(A.isdisjoint(B))
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

# Join A with B and B with A
D = B.union(A)
print(D)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A, B, C, D

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(f"Length of age list: {len(age)}")
print(f"Length of age set: {len(age_st)}")

# Explain the difference between the following data types: string, list, tuple and set
'''
- String: a data type, any data type written as text.
- List: a data collection which is ordered and changeable, allows duplicate members. Written with square brackects []
- Tuple: collection of different data types which is ordered and immutable. Once created, its values cannot be changed. Written with round brackets ().
- Set: a collection of items, unordered and unindexed. Does not allow duplicates.
'''


# How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
random_text = "I am a teacher and I love to inspire and teach people."
words_in_text = random_text.split()
print(f"Total words used: {len(words_in_text)}")
words_set = set(words_in_text)
print(f"Unique words used: {len(words_set)}")

