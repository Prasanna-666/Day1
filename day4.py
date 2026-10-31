#STRINGS
'''name = "Prasanna"
message = 'Hello, world!'
print(name)
print(message)'''

# Indexing and Slicing:
'''text = "Python"
print(text[0])      # Output: P
print(text[-1])     # Output: n
print(text[1:4])    # Output: yth'''

# Common String Methods:
'''Method	               Description
upper()	               Converts to uppercase
lower()	               Converts to lowercase
capitalize()           Capitals the first letter
title()                Capitals the first letter of every word
strip()            	   Removes whitespace from ends
replace(old, new)	   Replaces substring
split()	               Splits string into list
join()                 Joins the splitted string
find()	               Returns index of substring
len()	               Returns length of string'''

'''name = "  Python  "       
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.strip()) 
print(name.replace("n", "m"))
print(name.split())    
print(name.find("t"))       
print(len(name))''' 

# f-strings
'''name = "Prasanna"
age = 21
print(f"My name is {name} and I am {age} years old.")'''
#format()
'''name = "Prasanna"
age = 21
print("My name is {} and I am {} years old.".format(name, age))'''


'''str1 = "   If you trouble the trouble, trouble will troubles you. I am not the trouble, I am the truth --- by JAI Balayya@666   "

# Upper()
upper = str1.upper()
print(upper)

# Lower()
lower = str1.lower()
print(lower)

# Capitalize()
capitalize = str1.capitalize()
print(capitalize)

# Title()
print(str1.title())

# Strip()
strip = str1.strip()
print(strip)
# Right Strip()
print(str1.rstrip())
# Left Strip()
print(str1.lstrip())

# Split()
words = str1.split()
print(words)

# Join()
combined_string = "".join(words)
print(combined_string)'''

# Checking Methods
'''str1 = "If you trouble the trouble, trouble will troubles you. I am not the trouble, I am the truth --- by JAI Balayya@666"
print(str1.isupper())
print(str1.islower())
print(str1.isalnum())
print("hdbfgihAKJSFNJDXN234659".isalnum())
print("235468".isdigit())
print(str1.count("trouble"))

words = str1.split()
print(len(words))'''