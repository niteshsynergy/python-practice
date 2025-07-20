a=4
b=3
print("Sum of a+b:",a+b)
print("Sub of a-b:",a-b)
print("Mult a*b:",a*b)
print("Div a/b:",a/b)
print("Pow a**b:",a**b)
print("Floor div a//b:",a//b)
print("Mod div a%b:",a%b)


print("Comp of a==b:",a==b)
print("Comp of a!=b:",a!=b)
print("Comp of a>b:",a>b)
print("Comp of a<b:",a<b)
print("Comp of a&b:",a&b)
print("Comp of a|b:",a|b)
print("Comp of a^b:",a^b)
print("Comp of a>=b:",a>=b)
print("Comp of a<=b:",a<=b)
print("Comp of a!=b:",a!=b)


print("Comp of a>>b:",a>>b)
print("Comp of a<<b:",a<<b)
print("Comp of ~a:",~a)
print("Comp of ~b:",~b)
# print("Comp of `a",`a) Python version 3.13 does not support backquotes, use repr() instead

a+=100
print("Value of a+=100:",a)
a-=100
print("Value of a-=100:",a)
a*=100
print("Value of a*100:",a)
a//=100
print("Value of a//100:",a)
a**=100
print("Value of a**100:",a)
a%=100
print("Value of a%100:",a)




# 2. Python Operators
# a) Arithmetic Operators
# Operator	Description	Example
# +	Addition	5 + 3 = 8
# -	Subtraction	10 - 5 = 5
# *	Multiplication	4 * 2 = 8
# /	Division	10 / 2 = 5.0
# //	Floor Division	10 // 3 = 3
# %	Modulus	10 % 3 = 1
# **	Exponentiation	2 ** 3 = 8
# b) Comparison (Relational) Operators
# Operator	Description	Example
# ==	Equal to	5 == 5 → True
# !=	Not equal to	5 != 3 → True
# >	Greater than	10 > 5 → True
# <	Less than	3 < 7 → True
# >=	Greater than or equal to	5 >= 5 → True
# <=	Less than or equal to	3 <= 4 → True
# c) Logical Operators
# Operator	Description	Example
# and	Both conditions must be True	(5 > 2) and (3 < 7) → True
# or	At least one condition is True	(5 > 2) or (3 > 7) → True
# not	Reverses boolean value	not (5 > 2) → False
# d) Bitwise Operators
# Operator	Description	Example
# &	AND	5 & 3 → 1
# `	`	OR
# ^	XOR	5 ^ 3 → 6
# ~	NOT	~5 → -6
# <<	Left Shift	5 << 1 → 10
# >>	Right Shift	5 >> 1 → 2
# e) Assignment Operators
# Operator	Description	Example
# =	Assign	x = 5
# +=	Add and assign	x += 3 (x = x + 3)
# -=	Subtract and assign	x -= 2 (x = x - 2)
# *=	Multiply and assign	x *= 3 (x = x * 3)
# 3. Conditional Statements
#
# x = 10
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")