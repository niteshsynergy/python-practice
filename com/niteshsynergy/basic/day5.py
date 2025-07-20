# 5. Functions
def printEvenOdd(num):
    if num % 2 == 0:
        print(num,"is even")
    else:
        print(num,"is odd")


print(printEvenOdd(5)) # two response one is fuction response & another one is None as fucntion not returing anything.
printEvenOdd(50)


def returnHello(name):
    return "Hello " + name + " Welcome to Python"


print(returnHello("Synergy"))

# b) Lambda Functions

square  = lambda x: x * x
print("square (5): ",square (5))

# c) Types of Functions

#     Built-in Functions: len(), print(), type()


print(len("Welcome to Python"))
print(len("Welcome"))
print(len("Python"))
print(len(""))
print(len(" "))
print(len('a'))
# print(len(10))
print(type("Welcome"))
#     User-Defined Functions

def hello(name):
    return "Hello " + name + " Welcome to Python"
print(hello("Synergy"))

# Example of a user-defined function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

#     Recursive Functions

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("factorial(5) : ",factorial(5))

#     Lambda Functions

lambdaExp= lambda x: x * x
print(lambdaExp(5))

#     Higher-Order Functions: Functions that take another function as input.

# Example of a higher-order function (map function)
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
doubled_numbers = list(map(double, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8]

