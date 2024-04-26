# 1. Write a Python program to sum all the items in a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
def sum_items(items):
    sum = 0
    for i in items:
        sum += i
    return sum

for i in range(10):
    i = random.randint(-10,10)
    generated_list.append(i)
print("Wygenerowana lista: ", generated_list)
print("Suma elementow w liscie wynosi: ", sum_items(generated_list))

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
copy_of_generated_list = []

def random_generator(list_value):
    for i in range(10):
        i = random.randint(-50,50)
        list_value.append(i)
    return list_value

def compare_lists(l1, l2):
    comp_res = False
    for i in l1: 
        for j in l2: 
            if i == j:
                comp_res = True
                return comp_res

print("Lista 1: ", random_generator(generated_list))
print("Lista 2: ", random_generator(copy_of_generated_list))   
print(compare_lists(generated_list, copy_of_generated_list))

# 2. Write a Python program to multiply all the items in a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
def mult_items(items):
    mult = 1
    for i in items:
        mult *= i
    return mult

for i in range(3):
    i = random.randint(1,3)
    generated_list.append(i)
print("Wygenerowana lista: ", generated_list)
print("Iloczyn elementow w liscie wynosi: ", mult_items(generated_list))

# 20. Write a Python program to access the index of a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.randint(-5,10)
    generated_list.append(i)

print("Wygenerowana lista: ", generated_list)
for index, value in enumerate(generated_list):
    print("Index: ", index, ", wartosc: ", value)

# 21. Write a Python program to convert a list of characters into a string.

import os
import random
import string
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.choice(string.ascii_letters)
    generated_list.append(i)
    
print("Wygenerowana lista: ", generated_list)
convert_to_str = ''.join(generated_list)
print("Wygenerowany string: ", convert_to_str)

# 22. Write a Python program to find the index of an item in a specified list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.randint(-5,10)
    generated_list.append(i)

print("Wygenerowana lista: ", generated_list)
value_index = int(input("Index ktrórej wartosci z listy chcesz wyswietlic? (Tylko piewsze wystapienie): "))
print("Index wskazanej wartosci to:", generated_list.index(value_index))

# 24. Write a Python program to append a list to the second list.

import os
import random
import string
os.system('cls')
os.system('clear')

generated_list = []
copy_of_generated_list = []

def random_generator(list_value):
    for i in range(5):
        i = random.randint(-5,5)
        list_value.append(i)
    return list_value

def random_ascii_generator(ascii_list):
    for i in range(5):
        i = random.choice(string.ascii_letters)
        ascii_list.append(i)
    return ascii_list

print()
print("#" * 65 )
print()
print("Lista 1: ", random_generator(generated_list))
print("Lista 2: ", random_ascii_generator(copy_of_generated_list))
print()
print("#" * 65 )
print()

final_list = generated_list + copy_of_generated_list
print("Lista 3, skladajaca sie z polaczonych list 1 oraz 2: ", final_list)

# 25. Write a Python program to select an item randomly from a list.
# Use random.choice() to get a random element from a given list.

import os
import random
import collections
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.randint(-5,5)
    generated_list.append(i)

print("Wygenerowana lista: ", generated_list)
counter = collections.Counter(generated_list)
print("Czestotliwosc wystepowania elementow w liscie: ", counter)

# 27. Write a Python program to find the second smallest number in a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
def smallest_list(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest

for i in range(10):
    i = random.randint(1,10)
    generated_list.append(i)
print("Wygenerowana lista: ", generated_list)
print("Najmniejszy element w liscie to: ", smallest_list(generated_list))
generated_list.sort()
generated_list = set(generated_list)
generated_list = list(generated_list)
# print(generated_list) 
print("Drugi najmniejszy element w liscie to: ", generated_list[1])

# 28. Write a Python program to find the second largest number in a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
def largest_list(items):
    largest = items[0]
    for i in items:
        if i > largest:
            largest = i
    return largest

for i in range(10):
    i = random.randint(1,10)
    generated_list.append(i)
print("Wygenerowana lista: ", generated_list)
print("Najwiekszy element w liscie to: ", largest_list(generated_list))
generated_list.sort()
generated_list = set(generated_list)
generated_list = list(generated_list)
print("Drugi najwiekszy element w liscie to: ", generated_list[-2])

# 3. Write a Python program to get the largest number from a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
def largest_list(items):
    largest = items[0]
    for i in items:
        if i > largest:
            largest = i
    return largest

for i in range(10):
    i = random.randint(1,10)
    generated_list.append(i)
print("Wygenerowana lista: ", generated_list)
print("Najwiekszy element w liscie to: ", largest_list(generated_list))

# 30. Write a Python program to get the frequency of elements in a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.randint(1,5)
    generated_list.append(i)

print("Wygenerowana lista: ", generated_list)

# 4. Write a Python program to get the smallest number from a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
def smallest_list(items):
    smallest = items[0]
    for i in items:
        if i < smallest:
            smallest = i
    return smallest

for i in range(10):
    i = random.randint(-10,10)
    generated_list.append(i)
print("Wygenerowana lista: ", generated_list)
print("Najmniejszy element w liscie to: ", smallest_list(generated_list))

# 46. Write a Python program to select the odd items from a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.randint(1,5)
    generated_list.append(i)

print("Wygenerowana lista: ", generated_list)
print("Wyswietlam nieparzyste elelmenty z listy:", generated_list[::2])

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

import os
os.system('cls')
os.system('clear')

generated_list = []
list_len = int(input("Wprowadz zadana dlugosc listy: "))

for i in range(list_len):
    generated_list.append(input("Wprowadz wartosc do zapisania w liscie: "))

def count_strings(list_value):
    counter = 0
    for i in list_value:
        if len(i) > 1 and i[0] == i[-1]:
            counter += 1
    return counter
print("Wygenerowana lista: ", generated_list)
print("Liczba elementow spelniajacych kryteria z zadania wynosi: ",  count_strings(generated_list))

# 64. Write a Python program to iterate over two lists simultaneously.

import os
import random
import string
os.system('cls')
os.system('clear')

generated_list = []
copy_of_generated_list = []

def random_generator(list_value):
    for i in range(10):
        i = random.randint(-50,50)
        list_value.append(i)
    return list_value

def random_ascii_generator(ascii_list):
    for i in range(10):
        i = random.choice(string.ascii_letters)
        ascii_list.append(i)
    return ascii_list

print()
print("#" * 65 )
print()
print("Lista 1: ", random_generator(generated_list))
print("Lista 2: ", random_ascii_generator(copy_of_generated_list))
print()
print("#" * 65 )
print()

for (x, y) in zip(generated_list, copy_of_generated_list):
    print("Wartosc z pierwszej listy: ", x, " wartosc z drugiej listy: ", y)

# 68. Write a Python program to extend a list without appending.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
copy_of_generated_list = []

def random_generator(list_value):
    for i in range(5):
        i = random.randint(-50,50)
        list_value.append(i)
    return list_value

print("Lista 1: ", random_generator(generated_list))
print("Lista 2: ", random_generator(copy_of_generated_list))   

generated_list[len(generated_list):] = copy_of_generated_list
print("Lacze listy dodając Liste 2 na końcu Listy 1: ", generated_list)

# 7. Write a Python program to remove duplicates from a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []

for i in range(10):
    i = random.randint(1,5)
    generated_list.append(i)

print("Wygenerowana lista: ", generated_list)
print("Wartosci unikatowe: ", set(generated_list))

# 8. Write a Python program to check if a list is empty or not.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
user_input = ""

print("Obecna zawartosc listy: ", generated_list)
while not user_input == "Y" or user_input == "N":
    user_input = input("Czy chcesz wprowadzic (randomowe) wartosci do listy (Y/N): ")
    user_input = user_input.upper()
    if user_input == "Y":
        for i in range(10):
            i = random.randint(1,5)
            generated_list.append(i)
        print("Lista ma zawartosc: ", generated_list)
    elif user_input == "N":
        print("Nie wprowadzono zadnej wartosci, lista jest pusta:", generated_list)
        quit()
    else:
        print("Niepoprawny wybor, sproboj ponownie")

# 9. Write a Python program to clone or copy a list.

import os
import random
os.system('cls')
os.system('clear')

generated_list = []
copy_of_generated_list = []

for i in range(10):
    i = random.randint(-5,5)
    generated_list.append(i)
    
print("Lista oryginalna: ", generated_list)
copy_of_generated_list = list[generated_list]
print("Kopia listy: ", copy_of_generated_list)

# https://www.w3resource.com/python-exercises/list/
