'''
Write a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'
'''

# V1
import string, random

chars = list(string.ascii_lowercase)
numbers = list(string.digits)
chars.extend(numbers)

def random_user_id():
    pre_id = list()
    i = 0
    while i < 6:
        random_position = random.randint(0, len(chars) - 1)
        char = chars[random_position]
        pre_id.append(char)
        i += 1
        user_id = ''.join(pre_id)
    
    return user_id

print(random_user_id())

# V2
chars = list(string.ascii_lowercase + string.digits)

def random_user_id():
    user_id = ''.join(random.choice(chars) for _ in range(6))
    return user_id

print(random_user_id())


# V3
def random_user_id(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))



# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).


# Exercises: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.


# Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.