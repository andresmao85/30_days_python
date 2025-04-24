# Create an empty tuple
my_empty_tuple = ()
print(type(my_empty_tuple))

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Juan", "Mike", "Peter")
sisters = ("Sandra", "Monique")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
number_of_siblings = len(siblings)
print(f"I have {number_of_siblings} siblings")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Leon", "Lily")
print(family_members)

# Unpack siblings and parents from family_members
*siblings_unpacked, parent_1, parent_2 = family_members
print(siblings_unpacked)
print(parent_1)
print(parent_2)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ("potato", "carrot", "spinach")
animals = ("cow", "pig", "chicken", "fish")
food_stuff_tp = fruits + vegetables + animals

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
last_item_index = len(food_stuff_tp) - 1
middle_item_index = int(last_item_index / 2)
print(food_stuff_tp[middle_item_index])

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)

# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)
