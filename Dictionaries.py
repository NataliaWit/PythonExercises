#1 Write a  Python program to sort (ascending and descending) a dictionary by value.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1) , reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

# 10 Write a  Python program to sum all the items in a dictionary.
my_dict = {'data1' : 100, 'data2': 130, 'data3': 200}
result = sum(my_dict.values())
print(result)

# 11 Write a  Python program to multiply all the items in a dictionary.
my_dict = { 'data1' : 1, 'data2' : 2,  'data3' : 3}
result = 1
for key in my_dict:
        result= result * my_dict[key]
print(result)

#12Write a Python program to remove a key from a dictionary.py
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print (myDict)
if 'b' in myDict:
     del myDict['b']
print(myDict)

#13. Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
color = dict(zip(keys, values))
print(color)

#15 Write a  Python program to get the maximum and minimum values of a dictionary.
my_dict= {'x': 2 , 'y' : 5 , 'z' : 3}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
print('Maximum Value: ', my_dict[key_max])
print('Minimum Value: ', my_dict[key_min])

#16. Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'
    
    def do_nothing(self):
        pass

test = dictObj()
print(test.__dict__) 

#18 Write a  Python program to check if a dictionary is empty or not.
my_dict = {}
if not bool(my_dict):
    print('Dictonary is empty')
    
#19 Write a  Python program to combine two dictionary by adding values for common keys.
from collections import Counter
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 2, 'b': 2, 'c': 4}
d = Counter(d1) + Counter(d2)
print(d)

#2 Write a  Python program to add a key to a dictionary.
d = {0: 10, 1: 20}
print(d)
d.update({2: 30})
print(d)

#22 Write a  Python program to find the highest 3 values of corresponding keys in a dictionary.py
from heapq import nlargest
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)

#25 Write a  Python program to print a dictionary in table format.
my_dict = {'A': [1, 2, 3], 'B': [5, 6, 7], 'C': [9, 10, 11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)
    
#28. Write a Python program to sort a list alphabetically in a dictionary.
d1 = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in d1.items()}
print(sorted_dict)

#29. Write a Python program to remove spaces from dictionary keys.py
student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original: ", student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New: ", student_dict) 

#3. Write a Python script to concatenate the following dictionaries to create a new one.py
d1 = {1: 2, 3: 4,}
d2 = {10:10,20:20}
d3 = {44:22, 55:20}
d4={}
for d in (d1, d2, d3): d4.update(d)
print(d1, d2, d3, "---->",d4)

#4 Write a  Python program to check whether a given key already exists in a dictionary.
d = {1 : 10 , 2  : 20, 3 : 30, 4 : 40}
def is_key_present(x):
    if x in d:
        print ('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
is_key_present (100)
is_key_present (1)

#5Write a  Python program to iterate over dictionaries using for loops.py
d = {'x': 10, 'y': 20, 'z': 30}
for dict_key, dict_value in d.items():
    print(dict_key, '->', dict_value)

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
d1= {}
for x in range(1, 16):
    d1[x] = x**2
print(d1)

# 8 Write a  Python script to merge two  Python dictionaries.
d1 = { 'a': 1, 'b': 10 }
d2 = {'x' : 2, 'y': 20}
d = d1.copy()
d.update(d2)
print(d)

#9. Write a Python program to iterate over dictionaries using for loops.
d = {'blue': 1, 'Green': 2, 'pink': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])
