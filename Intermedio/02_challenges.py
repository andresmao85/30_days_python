# Reto: Fizz Buzz

'''
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz"
- Múltiplos de 5 por la palabra "buzz"
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1

# for index in range (1, 101)

# fizzbuzz()

# ****************************************************************

# Reto: ¿Es un anagrama?
'''
Escribe una función que reciba dos palabras (string) y retorne
verdadero o falso según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS 
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan
- Dos palabras exactamente iguales no son anagramas.
- No importa que sean mayúsculas o minúsculass
'''

def is_anagram(word_1: str, word_2: str):
    if word_1.lower() == word_2.lower():
        return False
    
    # V1
    # word_1_list = sorted([letter for letter in word_1.lower()])
    # word_2_list = sorted([letter for letter in word_2.lower()])
    # return word_1_list == word_2_list

    # V2
    return sorted(word_1.lower()) == sorted(word_2.lower())
    

# print(is_anagram("Noe23l", "l32eon"))

# ****************************************************************

# Reto: Sucesión de Fibonacci
'''
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el 
siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13 ...
'''

def fibo():
    series = [0, 1]
    for _ in range(0, 51):
        num = series[-1] + series[-2]
        series.append(num)
        
    return series
    
        
# V2
def fibonacci():
    prev = 0
    next = 1

    for _ in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

# V2
'''
def fibonacci():
    prev, next = 0, 1
    while True:
        yield prev
        prev, next = next, prev + next

num = int(input('Número de valores: '))
for index, x in enumerate(fibonacci()):
    if index == num:
        break
    print('%s' % x)
'''

# Reto: Números primos

'''
Verificar si un número es primo o no.
Imprimir los 100 primeros primos.
'''

def is_prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True

    if num % 2 == 0: 
        return False
    
    divisor = 3
    while divisor * 3 <= num:
        if num % divisor == 0:
            return False
        divisor += 2
    
    return True

print(is_prime(7))

def primos():
    for i in range(1, 101):
        if is_prime(i):
            print(i)

primos()


# Invertir cadena de texto
'''
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Hola mundo > odnum aloH
'''

def invert_order(text):
    inverted  = []
    for letter in text:
        inverted.insert(0, letter)

    return ''.join(inverted)

print(invert_order("Hola mundo"))

# V2
def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]

    return reversed_text

print(reverse("Hola mundo"))