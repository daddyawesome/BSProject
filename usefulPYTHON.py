# 1. Swap values between two variables
a = 5                              
b = 10                                                           
a, b = b, a
print(a) # 10           
print(b) # 5

#2. Check if the given number is even
def is_even(num):
  return num % 2 == 0
is_even(10) # True

#3. Split a multiline string into a list of lines
def split_lines(s):
  return s.split('\n')
split_lines('50\n python\n snippets') # ['50', ' python', ' snippets']

#4. Find memory used by an object
import sys
print(sys.getsizeof(5)) # 28
print(sys.getsizeof("Python")) # 55

#5. Reverse a string
language = "python"                                
reversed_language = language[::-1]                                                                 
print(reversed_language) # nohtyp

#6. Print a string n times
def repeat(string, n):
  return (string * n)
repeat('python', 3) # pythonpythonpython

#7. Check if a string is a palindrome
def palindrome(string):
    return string == string[::-1]
palindrome('python') # False

#8. Combine a list of strings into a single string
strings = ['50', 'python', 'snippets']
print(','.join(strings)) # 50,python,snippets

#9. Find the first element of a list
def head(list):
  return list[0]
print(head([1, 2, 3, 4, 5])) # 1

#10. Find elements that exist in either of the two lists
def union(a,b):
  return list(set(a + b))
union([1, 2, 3, 4, 5], [6, 2, 8, 1, 4]) # [1,2,3,4,5,6,8]

#11. Find all the unique elements present in a given list
def unique_elements(numbers):
  return list(set(numbers))
unique_elements([1, 2, 3, 2, 4]) # [1, 2, 3, 4]

#12. Find the average of a list of numbers
def average(*args):
  return sum(args, 0.0) / len(args)
average(5, 8, 2) # 5.0

#13. Check if a list contains all unique values
def unique(list):
    if len(list)==len(set(list)):
        print("All elements are unique")
    else:
        print("List has duplicates")
unique([1,2,3,4,5]) # All elements are unique

#14. Track frequency of elements in a list
from collections import Counter
list = [1, 2, 3, 2, 4, 3, 2, 3]
count = Counter(list)
print(count) # {2: 3, 3: 3, 1: 1, 4: 1}

#15. Find the most frequent element in a list
def most_frequent(list):
    return max(set(list), key = list.count)
numbers = [1, 2, 3, 2, 4, 3, 1, 3]
most_frequent(numbers) # 3

#16. Convert an angle from degrees to radians
import math
def degrees_to_radians(deg):
  return (deg * math.pi) / 180.0
degrees_to_radians(90) # 1.5707963267948966

#
#
#
#
#
#
#
#
#
#
