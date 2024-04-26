# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included). 

import os
os.system('cls')
os.system('clear')

def mult_div(val1, val2):
    list_of_numbers=[]
    for i in range(val1, val2):
        if i % 5 == 0 and i % 7 == 0:
            list_of_numbers.append(i)
    return list_of_numbers

print(mult_div(int(input("Wprowadz wartosc poczatkowa: ")), int(input("Wprowadz wartosc koncowa: "))))

# 10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

import os
os.system('cls')
os.system('clear')

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# 14. Write a Python program that accepts a string and calculates the number of digits and letters.

import os
os.system('cls')
os.system('clear')

user_input = input("Wprowadz ciag znakow zawierajacy cyfry i litery: ")

letter_counter = 0
number_counter = 0

for i in user_input:
    if i.isdigit():
        number_counter += 1 
    elif i.isalpha():
        letter_counter += 1
    else:
        continue
print("Ilosc liczb: ", number_counter)
print("Ilosc liter: ", letter_counter)

# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

import os
os.system('cls')
os.system('clear')

value_list = []

for i in range(100, 401):
    i = str(i)
    if (int(i[0]) % 2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0):
        value_list.append(i)

print(",".join(value_list))

# 17. Write a Python program to print the alphabet pattern 'A'.

import os
os.system('cls')
os.system('clear')

letter_A = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            letter_A = letter_A + "*" 
        else:
            letter_A = letter_A + " "  
    letter_A = letter_A + ""  
print(letter_A) 

# 18. Write a Python program to print the alphabet pattern 'D'.

import os
os.system('cls')
os.system('clear')

letter_D = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
            letter_D = letter_D + "*" 
        else:
            letter_D = letter_D + " "  
    letter_D = letter_D + ""  
print(letter_D) 

# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 

import os
os.system('cls')
os.system('clear')

temp_in = input("Wpisz temperature do przekonwertowania, C lub F na koncu przekonwertuje na przeciwna jednostke (przykladowo: 30C lub 30F): ")

unit = temp_in[-1].upper()
value = int(temp_in[:-1])
if unit == "C":
    value = round((9 * value) / 5 + 32)
    unit = "Fahrenheit"
elif unit == "F":
    value = round((value - 32) * 5 / 9)
    unit = "Celsius"
else:
    print("Dozwolone jest wprowadzenie wartosci konczacych sie litera C lub F.")
print("Temperatura w jednostce:", unit, "wynosi: ", value,u'\N{DEGREE SIGN}')

# 27. Write a Python program to print the alphabet pattern 'T'.

import os
os.system('cls')
os.system('clear')

letter_T = ""
for row in range(0, 7):
    for column in range(0, 7):
        if (column == 3 or (row == 0 and column > 0 and column < 6 )):
            letter_T = letter_T + "*" 
        else:
            letter_T = letter_T + " "  
    letter_T = letter_T + ""  
print(letter_T) 

# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import os
import random
os.system('cls')
os.system('clear')

random_number = random.randint(1,10)
guess = 0

while random_number != guess: 
    guess = int(input("Zgadnij numer z przedzialu 1 - 10: "))

print("Zgadles, numer to: ", guess)

# 31. Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73

import os
os.system('cls')
os.system('clear')

def year_convert(value):
    dog_years = 0
    for i in range(1,value+1):
        if i <=2 and i > 0:
            dog_years += 10.5
        else: 
            dog_years += 4
    return round(dog_years)
print(year_convert(int(input("Wprowadz lata do przekonwertowania na psie lata: "))))

# 34. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.

import os
os.system('cls')
os.system('clear')

def sum_integers(value1, value2):
    sum = value1 + value2
    if sum in range(15, 20):
        return 20
    else: 
        return sum
print(sum_integers(int(input("Wprowadz pierwsza liczbe: ")), int(input("Wprowadz druga liczbe: "))))

# 36. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8                                                                    
# z: 12                                                                   
# Scalene triangle  

import os
os.system('cls')
os.system('clear')

def triangle_type(v1, v2, v3):
    if v1 == v2 == v3:
        return "Trojkat rownoboczny"
    elif v1 == v2 or v1 == v3 or v2 == v3: 
        return "Trojkat rownoramienny"
    else: 
         return "Trojkat skalenowy"
     
print(triangle_type(int(input("Wprowadz ramie A: ")), int(input("Wprowadz ramie B: ")), int(input("Wprowadz ramie C: "))))

# 4. Write a Python program to construct the following pattern, using a nested for loop.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

import os
os.system('cls')
os.system('clear')

user_input = int(input("Liczba kolumn: "))
star = "* "

# print(star * 10)
for i in range(user_input):
    print(star * i)
for i in range(user_input, 0, -1): # Od (user_input), do (0), w odwrotnej kolejnosci (-1)
    print (star * i)

# 40. Write a Python program to find the median of three values.
# Expected Output:

# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0   


import os
os.system('cls')
os.system('clear')

def find_median(v1, v2, v3):
    median = 0
    if v1 > v2:
        if v1 < v3:
            median = v1
        elif v2 > v3:
            median = v2
        else:
            median = v3
    else:
        if v1 > v3:
            median = v1
        elif v2 < v3:
            median = v2
        else:
            median = v3
    return "Mediana wynosi:", median 

print(find_median(int(input("Wprowadz pierwsza wartosc: ")), int(input("Wprowadz druga wartosc: ")), int(input("Wprowadz trzecia wartosc: "))))

# 43. Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:

# Input a number: 6                                                       
# 6 x 1 = 6                                                               
# 6 x 2 = 12                                                              
# 6 x 3 = 18                                                              
# 6 x 4 = 24                                                              
# 6 x 5 = 30                                                              
# 6 x 6 = 36                                                              
# 6 x 7 = 42                                                              
# 6 x 8 = 48                                                              
# 6 x 9 = 54                                                              
# 6 x 10 = 60 

import os
os.system('cls')
os.system('clear')

number = int(input("Wprowadz liczbe do stworzenia tabliczki mnozenia: "))

for i in range(1,11):
    print(number, "*", i, "=", number * i)

# 5. Write a Python program that accepts a word from the user and reverses it. 

import os
os.system('cls')
os.system('clear')

def reverse_it(value):
    return print("Twoja odwrocona wartosc: ", value[::-1])
print(reverse_it(input("Wprowadz wartosc: ")))

# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

import os
os.system('cls')
os.system('clear')

numbers = []
even = 0
odd = 0
def numbers_list(value):
    for i in range(1,value+1):
        numbers.append(i)
    return numbers
print(numbers_list(int(input("Wprowadz liczbe do utworzenia listy: "))))
for number in numbers:
    if number % 2 == 0:
        even += 1 
    else: 
        odd +=1
print("Ilość liczb parzystych w liście: ", even)
print("Ilość liczb nieparzystych w liście: ", odd)

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

import os
os.system('cls')
os.system('clear')

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(i, "jest typem danych: ", type(i))
    
# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.

import os
os.system('cls')
os.system('clear')

for i in range(6):
    if i == 3 or i == 6: 
        continue
    else:
        print(i, end= ' ')
        
# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

import os
os.system('cls')
os.system('clear')

x = 0
y = 1

while y < 50:
    print(y)
    x, y = y, x + y

# def fibonacci(n):
#     if n < 3 and n > 0:
#         return 1
#     elif n == 0:
#         return 0
#     elif n < 0: 
#         print("Nieprawidłowa wartość")
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(int(input("Wprowadz numer: "))))
# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
