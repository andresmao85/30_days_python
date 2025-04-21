'''
Write a function which generates a six digit/character random_user_id.
  print(random_user_id());
  '1ee33d'
'''

# V1
import string, random

chars = list(string.ascii_letters)
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
chars = list(string.ascii_letters + string.digits)

def random_user_id():
    user_id = ''.join(random.choice(chars) for _ in range(6))
    return user_id

print(random_user_id())


# V3
def random_user_id(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))



# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    chars_num = int(input("Number of chars: "))
    ids_num = int(input("Number of ID's: "))
    total_ids = []

    for _ in range(ids_num):
        user_id = ''.join(random.choice(chars) for _ in range (chars_num))
        total_ids.append(user_id)
        
    return '\n'.join(total_ids)
    

# print(user_id_gen_by_user())

# V2
def user_id_gen_by_user2():
    try:
        chars_num = int(input("Number of characters per ID: "))
        ids_num = int(input("Number of IDs to generate: "))
    except ValueError:
        return "Please enter valid integer numbers."

    total_ids = [
        ''.join(random.choice(chars) for _ in range(chars_num))
        for _ in range(ids_num)
    ]
    
    return '\n'.join(total_ids)

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    return f"rgb({random.choice(range(256))},{random.choice(range(256))},{random.choice(range(256))})"

# V2
def rgb_color_gen2():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


print(rgb_color_gen())


# Exercises: Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.


# Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.