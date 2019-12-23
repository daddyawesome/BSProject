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
#
#
#
#
