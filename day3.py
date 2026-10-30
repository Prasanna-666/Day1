#OPERATORS
#Arithmetic Operators
'''Operator   Description   Example   Output
+	        Addition	    10 + 5	  15
-	       Subtraction	    10 - 5	   5
*	     Multiplication	    10 * 5	  50
/	        Division	    10 / 5	  2.0
//	    Floor Division	    10 // 3	  3
%  	 Modulus (remainder)    10 % 3	  1
**	    Exponentiation	    2 ** 3	  8'''
'''a = 10
b = 20
sum = (a + b)
print(sum)'''

#Assignment Operators
'''Operator	   Meaning	         Example
=	           Assign             x = 10
+=	        Add and assign	      x += 5 → x = x + 5
-=	     Subtract and assign      x -= 5
*=	     Multiply and assign	  x *= 2
/=	     Divide and assign	      x /= 3
//=	   Floor divide and assign	  x //= 2
%=	     Modulus and assign    	  x %= 2
**=    	  Power and assign	      x **= 2'''
'''x = 3
x += 3
print(x)'''

#Comparison (Relational) Operators
'''Operator      Meaning	    Example	     Output
==	         Equal to	    5 == 5	    True
!=	       Not equal to	    5 != 3	    True
>	       Greater than	    5 > 3	    True
<	        Less than	    5 < 3	    False
>=	     Greater or equal	5 >= 5	    True
<=	      Less or equal	    3 <= 5	    True'''
'''a = 3
b = 3
print(a == b)'''

#Logical Operators
'''Operator	Description	          Example	      Output
and	    True if both are true	True and False	   False
or	    True if one is true	    True or False	   True
not	    Reverses the result	       not True	       False'''
'''x = 5
print(x > 3 and x < 10)'''

#Bitwise Operators
'''Operator	            Description	                 Example
&   AND	             True if both are true          5 & 3 → 1
|   OR               True if one is true            5 | 3 → 7
^	XOR	             True if it is opposite         5 ^ 3 → 6
~	NOT	             ~n ---> -(n + 1)               ~5 → -6
<<	Left Shift	     Moving left                    5 << 1 → 10
>>  Right Shift	     Moving right                   5 >> 1 → 2'''
'''a = 5
b = 3
print(a & b)'''

#Membership Operators
'''Operator	Description	         Example	       Output
in	       True if present	  "a" in "apple"	   True
not in	  True if not present "x" not in "apple"   True'''
'''text = "Python"
print("y" in text)'''

# Identity Operators
'''Operator	Description	         Example   
is	    True if same object	      x is y           
is not	True if not same object	  x is not y'''

#Practice

# 1) Arithmetic Operator (+, -, *, /, //, %, **)
'''x = 10
y = 100
print(x + y, x - y, x * y, x / y, x // y, x % y, y ** x)'''

# 2) Assignment Operator (+=, -=, *=, /=, //=, %=)
'''x = 200
print(x)
x += 100 # x = x + 100
print(x)
x -= 200 # x = x - 200
print(x)
x *= 4 # x = x * 4
print(x)
x //= 2 # x = x // 2
print(x)
x %= 2
print(x)'''

# 3) Comparision or Relational Operator (==, !=, >, <, >=, <=)
'''x = 26
y = 14
print(x == y, x != y, x > y, x < y, x >= y, x <= y)'''

# 4) Logical Operator (and, or, not)
'''x = 20
y = 21
print((x < y) and (x == y))
print((x > y) and (x != y))
print((x < y) or (x >= y))
print (not (x < y))
print(not (x > y))'''

# 5) Bitwise Operator (&, |, ^, ~, <<, >>)
'''num1 = 45
num2 = 4
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)
print(~num2)
print(num2 << 2)
print(num2 >> 1)'''

# 6) Membership Operator (in, not in)
'''l = [10, 2, 3, 4, 5]
print(100 not in l)
print(4 in l)
print(5 not in l)'''

# 7) Identity Operator (is, is not)
'''x = 5
y = 5
print(x is y)
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)
a = [1, 2, 3]
b = a
print(a is b)'''

