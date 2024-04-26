# 1. Write a Python program to calculate the length of a string. 

import os
os.system('cls')
os.system('clear')

def count_letters(str_value):
    counter = 0
    for i in str_value:
        counter += 1
    return "Twoj ciag sklada sie z: ",counter, "znakow"
print(count_letters(input('Wprowadz ciag znakow do policzenia: ')))

# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged. 

import os
os.system('cls')
os.system('clear')

def exchange_first_last(string_value):
    return string_value[-1:] + string_value[1:-1] + string_value[:1]     
print(exchange_first_last(input('Wprowadz ciag znakow: ')))# 11. Write a Python program to remove characters that have odd index values in a given string. 

import os
os.system('cls')
os.system('clear')

def odd_index_rmv(string_value):
    odd = ""

    for index in range(len(string_value)):
        if index % 2 == 0:
            odd = odd + string_value[index]
    return odd
print(odd_index_rmv(input('Wprowadz ciag znakow: ')))

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases. 

import os
os.system('cls')
os.system('clear')

string_value = input("Wpropwadz tekst, ktory zostanie przekonwertowany na duze i male litery: ")

print("Wprowadzona wartosc: ", string_value)
print("Duze litery: ", string_value.upper())
print("Male litery: ", string_value.lower())

# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

import os
os.system('cls')
os.system('clear')

def insert_middle(char,string_value):
    return char[:2] + string_value + char[2:]
print(insert_middle(input("Wprowadz dwa poczatkowe i koncowe znaki pomiedzy ktore wprowadzisz string: "),input("Wprowadz ciag znakow: ")))# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

import os
os.system('cls')
os.system('clear')

def last_two_four_times(string_value):
    ltft = string_value[-2:] 
    ltft = ltft * 4
    return ltft

print(last_two_four_times(input("Wprowadz ciag znakow, ostatnie dwa znaki zostana powtorzone i wyswietlone 4 razy: ")))
# 18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

import os
os.system('cls')
os.system('clear')

def first_three(string_value):
    if len(string_value) < 3:
        print(string_value)
    else: 
        ft = string_value[:3]
        return ft
print(first_three(input('Wprowadz ciag znakow: ')))

# 2. Write a Python program to count the number of characters (character frequency) in a string. 

import os
os.system('cls')
os.system('clear')

def count_letters(str_value):
    dictionary = {}
    
    for i in str_value:
        letter = dictionary.keys()
        
        if i in letter:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    return dictionary
print(count_letters(input('Wprowadz ciag znakow do policzenia: ')))

# 20. Write a Python function to reverse a string if its length is a multiple of 4. 

import os
os.system('cls')
os.system('clear')

def reverse_str(string_value):
    if len(string_value) % 4 == 0: 
        # string_value = string_value[::-1]
        return string_value[::-1] # od konca, co jeden
    else:
        return string_value
print(reverse_str(input("Wprowadz ciag znakow: ")))

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 

import os
os.system('cls')
os.system('clear')

def if_upper(string_value):
    count_upper = 0
    for char in string_value[:4]:
        if char.upper() == char:
            count_upper += 1
    if count_upper >= 2:
        return string_value.upper()
    return string_value
print(if_upper(input("Wprowadz ciag znakow: ")))

# 24. Write a Python program to check whether a string starts with specified characters.

import os
os.system('cls')
os.system('clear')

# string_value = input("Wprowadz ciag znakow: ")
def string_check(string_value, string_test):
    if string_value.startswith(string_test) == True:
        return string_value, ": rozpoczyna sie od: ", string_test
    # else: 
    # print(string_value, ": NIE rozpoczyna sie od: ", string_test)
    return string_value, ": NIE rozpoczyna sie od: ", string_test 

print(string_check(input("Wprowadz ciag znakow: "), input("Wprowadz ciag znakow, w celu przetestowania, czy poprzedni input rozpoczyna się od tego ciagu znakow: ")))# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. 

import os
os.system('cls')
os.system('clear')

def add_last_two(string_value):
    if len(string_value) < 2:
        return ''
    return string_value[0:2] + string_value[-2:]
    # print ("Dwie pierwsze i dwie ostatnie litery ciagu znaków", string_value, "to: ", string_value[0:2] + string_value [-2:])
print(add_last_two(input('Wprowadz ciag znakow: ')))

# 39. Write a Python program to reverse a string. 

import os
os.system('cls')
os.system('clear')

string = input("Wprowadz ciag znakow: ")
print("Odwrocony ciag znakow: ", string[::-1])

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

import os
os.system('cls')
os.system('clear')

def replace_char(string_value):
    char = string_value[0] # Wyciagnij pierwszy znak z ciagu znakow
    string_value = string_value.replace(char, "$") # Zastap litere ze zmiennej char znakiem $
    string_value = char + string_value[1:] # Ciag znakow staje sie litera ze zmiennej char + pozostaly ciag znakow ze zmiennej string_value (od drugiego znaku) 
    return string_value # Zwroc wartosc
print(replace_char(input('Wprowadz ciag znakow, kolejne wystąpienie pierwszej litery w ciągu znakow zostanie zastapione symbolem $: ')))

# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

import os
os.system('cls')
os.system('clear')

def char_index(string_value):
    step = 0
    for index, char in enumerate(string_value):
        print("Znak: ", char, ", index: ", index)
    return "Zakonczono"
print(char_index(input("Wprowadz ciag znakow: ")))

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

import os
os.system('cls')
os.system('clear')

def string_swap(string1, string2):
    swapped_string1 = string2[:2] + string1[2:] 
    swapped_string2 = string1[:2] + string2[2:]
    return swapped_string1 + ' ' + swapped_string2

print(string_swap(input('Wprowadz PIERWSZY ciag znakow: '), input('Wprowadz DRUGI ciag znakow: ')))

# 57.Write a Python program to remove spaces from a given string. 

import os
os.system('cls')
os.system('clear')

def replace_spaces(string_value):
    string_value = string_value.replace(' ','')
    return string_value
print(replace_spaces(input("Wprowadz ciag znakow ze spacjami: ")))

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged. 

import os
os.system('cls')
os.system('clear')

def add_ing_or_ly(string_value):
    str_length = len(string_value)

    if str_length > 2:
        if string_value[-3:] == 'ing':
            string_value += 'ly'
        else:
            string_value += 'ing'
    return string_value
print(add_ing_or_ly(input('Wprowadz ciag znakow: ')))

# 83. Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001

import os
os.system('cls')
os.system('clear')

def reformat_int(int_value):
    decimal = str(int_value)
    octal = str(oct(int_value))[2:]
    hexadecimal = str(hex(int_value))[2:].upper()
    binary = str(bin(int_value))[2:]
    return "Wprowadzona wartość: ", int_value, "dziesietnie to: ", decimal, "osemkowo to: ", octal, "szesnastkowo to: ", hexadecimal, "binarnie to: ", binary
print(reformat_int(int(input("Wprowadz liczbe: "))))

# 9. Write a Python program to remove the nth index character from a nonempty string.  

import os
os.system('cls')
os.system('clear')

def remove_letter(string_value, index_value):
    up_to = string_value[:index_value]
    from_to = string_value[index_value + 1:]
    return up_to + from_to

print(remove_letter(input('Wprowadz ciag znakow: '), int(input('Wprowadz indeks litery, ktora chcesz usunac (liczone od 0): '))))

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

import os
os.system('cls')
os.system('clear')

def replace_char(string_value):
    char = string_value[0] # Wyciagnij pierwszy znak z ciagu znakow
    string_value = string_value.replace(char, "$") # Zastap litere ze zmiennej char znakiem $
    string_value = char + string_value[1:] # Ciag znakow staje sie litera ze zmiennej char + pozostaly ciag znakow ze zmiennej string_value (od drugiego znaku) 
    return string_value # Zwroc wartosc
print(replace_char(input('Wprowadz ciag znakow, kolejne wystąpienie pierwszej litery w ciągu znakow zostanie zastapione symbolem $: ')))

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. 

import os
os.system('cls')
os.system('clear')

def add_last_two(string_value):
    if len(string_value) < 2:
        return ''
    return string_value[0:2] + string_value[-2:]
    # print ("Dwie pierwsze i dwie ostatnie litery ciagu znaków", string_value, "to: ", string_value[0:2] + string_value [-2:])
print(add_last_two(input('Wprowadz ciag znakow: ')))


