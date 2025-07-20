"""
Python Functions - Complete Guide
"""

# ------------------------------------------------
# 1. What is Function?
# ------------------------------------------------
# A function is a block of reusable code that performs a specific task.
# It helps in modular programming and code reusability.

# ------------------------------------------------
# 2. Advantages of Functions
# ------------------------------------------------
# - Code Reusability: Write once, use multiple times.
# - Improves Readability: Modular approach for better understanding.
# - Easy Debugging: Fix issues in one place without affecting the entire code.
# - Better Code Management.

# ------------------------------------------------
# 3. Syntax and Writing function
# ------------------------------------------------
# A function is defined using `def` keyword.

def greet():
    """This function prints a greeting message."""
    print("Hello, Welcome to Python Functions!")

# ------------------------------------------------
# 4. Calling or Invoking function
# ------------------------------------------------
greet()  # Calling the function

# ------------------------------------------------
# 5. Classification of Functions
# ------------------------------------------------

# a) No arguments and No return values
def say_hello():
    print("Hello, World!")

say_hello()  # Output: Hello, World!

# b) With arguments and No return values
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!

# c) With arguments and With return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)  # Output: 15

# d) No arguments and With return values
def get_pi():
    return 3.14159

pi_value = get_pi()
print(pi_value)  # Output: 3.14159

# e) Recursion (Function calling itself)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# ------------------------------------------------
# 6. Python Argument Type Functions
# ------------------------------------------------

# a) Default argument functions
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

# b) Required (Positional) arguments function
def subtract(a, b):
    return a - b

print(subtract(10, 5))  # Output: 5

# c) Keyword arguments function
def describe_person(name, age):
    print(f"Name: {name}, Age: {age}")

describe_person(age=25, name="Bob")  # Keyword arguments

# d) Variable arguments functions (*args)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# ------------------------------------------------
# 7. ‘pass’ keyword in functions
# ------------------------------------------------
# The `pass` keyword is used when a function is declared but not implemented yet.

def future_function():
    pass  # Placeholder for future code

# ------------------------------------------------
# 8. Lambda Functions (Anonymous Functions)
# ------------------------------------------------

# a) Simple lambda function
square = lambda x: x * x
print(square(5))  # Output: 25

# b) map() function (Applies function to all elements in a list)
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# c) filter() function (Filters elements based on condition)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# d) reduce() function (Reduces elements to a single value)
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 15

# ------------------------------------------------
# 9. Nested Functions
# ------------------------------------------------
def outer_function():
    print("Outer function")

    def inner_function():
        print("Inner function")

    inner_function()  # Calling inner function

outer_function()

# ------------------------------------------------
# 10. Non-local and Global Variables
# ------------------------------------------------

# a) Global variable
global_var = "I am Global"

def global_example():
    global global_var
    global_var = "Modified Global"
    print(global_var)

global_example()  # Output: Modified Global
print(global_var)  # Output: Modified Global

# b) Non-local variable (Used inside nested functions)
def outer():
    non_local_var = "Outer Value"

    def inner():
        nonlocal non_local_var
        non_local_var = "Modified Inside Inner"
        print(non_local_var)

    inner()
    print(non_local_var)

outer()

# ------------------------------------------------
# 11. Closures (Function returning another function)
# ------------------------------------------------
def multiplier(factor):
    def multiply_by(value):
        return value * factor
    return multiply_by

double = multiplier(2)
print(double(5))  # Output: 10

# ------------------------------------------------
# 12. Decorators (Modify behavior of function)
# ------------------------------------------------

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function executed!")

display()  # Calls wrapper first

# ------------------------------------------------
# 13. Generators (Using `yield` to return values one by one)
# ------------------------------------------------
def generate_numbers():
    for i in range(3):
        yield i

gen = generate_numbers()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# ------------------------------------------------
# 14. Iterators (Class implementing `__iter__` and `__next__`)
# ------------------------------------------------
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

counter = Counter(0, 3)
for number in counter:
    print(number)  # Output: 0, 1, 2

# ------------------------------------------------
# 15. Monkey Patching (Modifying a class method at runtime)
# ------------------------------------------------
class Dog:
    def speak(self):
        return "Woof!"

def new_speak():
    return "Meow!"  # Changing behavior dynamically

Dog.speak = new_speak  # Monkey patching
dog = Dog()
print(dog.speak())  # Output: Meow!
