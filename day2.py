# Numeric Data Types - integer, float, complex
'''number = 100
percentage = 9.4
c = 2+3j
print(number, type(number))
print(percentage, type(percentage))
print(c, type(c))'''

# Sequence Data Types - strings, list, tuple
'''s = "Prasanna"
lst = [10, 20.3, "30"]
t = (1, 2, 3, 4)
t1 = (100,)
print(type(s), type(lst), type(t), type(t1))'''

# Boolean Data Types - True, False
'''bool1 = True
bool2 = False
print(bool1, type(bool1))
print(bool2, type(bool2))
print(bool1 + bool2)'''

# Mapping Data Types - Dictionary
'''d = {"name":"CodeGnan",
     "location":"Hyd",
     "branch":4}
print(d, type(d))'''

# Sets
'''s = {1, 2, 3, 4}
print(s, type(s))'''

# Empty Data
'''lst = []   # list()
t = ()   # tuple()
str = ""   # str()
d = {}   # dict()
s = set()
print(lst, type(lst))
print(t, type(t))
print(str, type(str))
print(d, type(d))
print(s, type(s))'''

# User Input
'''num = int(input("Enter: "))
print(num)
name = input()
print(name)'''

# Type Conversion
'''str = "Prasanna"
print(str)
lst = list(str)
print(lst)
t = tuple(lst)
print(t)
set = set(lst)
print(set)'''

#Implicit Type Casting
'''n1 = 100
n2 = 6.78
n3 = n1 + n2
print(type(n1), type(n2))
print(n3, type(n3))'''

# Explicit Type Casting
'''n = input()
print(type(n))
n1 = int(n)
print(type(n1))'''

# User Input
'''num = int(input())
s = input()
lst = list(map(int, input().split(",")))
t = tuple(map(int, input().split()))
set = set(map(int, input().split()))
print(num)
print(s)
print(lst)
print(t)
print(set)'''