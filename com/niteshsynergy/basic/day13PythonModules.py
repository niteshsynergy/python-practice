"""
Python Modules - Complete Guide
"""

# ------------------------------------------------
# 1. Importance of Modular Programming
# ------------------------------------------------
# - **Code Reusability**: Write once, use multiple times.
# - **Better Code Organization**: Makes code readable and manageable.
# - **Easy Maintenance**: Fix errors in one module without affecting others.
# - **Encapsulation**: Helps in keeping functionalities separate.

# ------------------------------------------------
# 2. What is a Module?
# ------------------------------------------------
# A **module** is a Python file containing functions, classes, or variables that can be reused in different programs.

# ------------------------------------------------
# 3. Types of Modules
# ------------------------------------------------
# a) **Predefined (Built-in) Modules**: Modules provided by Python like `math`, `os`, `sys`, etc.
# b) **User-defined Modules**: Custom modules created by users.

# ------------------------------------------------
# 4. User-defined Modules Creation
# ------------------------------------------------
# A module is simply a `.py` file that contains functions or classes.

# Example: Create a file `mymodule.py` and add the following content:
"""
# mymodule.py (User-defined module)
def greet(name):
    return f"Hello, {name}!"

class MathOperations:
    def add(self, a, b):
        return a + b
"""

# ------------------------------------------------
# 5. Functions-Based Modules
# ------------------------------------------------
# The above `mymodule.py` is a **function-based module** as it contains the `greet` function.

# ------------------------------------------------
# 6. Class-Based Modules
# ------------------------------------------------
# `mymodule.py` also contains a class `MathOperations`, making it a **class-based module**.

# ------------------------------------------------
# 7. Connecting Modules (Importing)
# ------------------------------------------------
# To use a module, we need to import it.

import mymodule  # Importing our custom module

# Using function from mymodule
print(mymodule.greet("Alice"))  # Output: Hello, Alice!

# Using class from mymodule
math_obj = mymodule.MathOperations()
print(math_obj.add(5, 3))  # Output: 8

# ------------------------------------------------
# 8. Import Module (Built-in Modules)
# ------------------------------------------------
# Python has many built-in modules like `math`, `random`, `os`.

import math

print(math.sqrt(16))  # Output: 4.0

# ------------------------------------------------
# 9. From ... Import (Importing specific functions/classes)
# ------------------------------------------------
from math import sqrt, pi

print(sqrt(25))  # Output: 5.0
print(pi)  # Output: 3.141592653589793

# ------------------------------------------------
# 10. Module Alias / Renaming Module
# ------------------------------------------------
# Modules can be renamed using `as`.

import math as m  # Renaming math module

print(m.factorial(5))  # Output: 120

# ------------------------------------------------
# 11. Built-in Properties of a Module
# ------------------------------------------------
# Every module has some built-in properties like `__name__`, `__doc__`, etc.

print(__name__)  # Output: __main__ (when running directly)
print(math.__name__)  # Output: math

# Checking module documentation
print(math.__doc__)  # Prints documentation of the math module

# ------------------------------------------------
# 12. Using `dir()` to list available attributes in a module
# ------------------------------------------------
print(dir(math))  # Lists all functions inside the math module

# ------------------------------------------------
# 13. Finding Module Location (Path)
# ------------------------------------------------
import os
print(os.__file__)  # Output: Path where the os module is stored

# ------------------------------------------------
# 14. Creating a Package (Folder containing multiple modules)
# ------------------------------------------------
# A **package** is a collection of multiple modules stored in a directory.
# It must contain a special file named `__init__.py`.

"""
Directory Structure:
my_package/
    __init__.py
    module1.py
    module2.py
"""

# Create `module1.py` inside `my_package/`
"""
# module1.py
def function1():
    return "This is function1 from module1"
"""

# Importing from a package
from my_package import module1
print(module1.function1())  # Output: This is function1 from module1

# ------------------------------------------------
# 15. Exploring Common Built-in Modules
# ------------------------------------------------

# a) random module (Generating random numbers)
import random
print(random.randint(1, 10))  # Random number between 1 and 10

# b) datetime module (Working with dates & time)
import datetime
print(datetime.datetime.now())  # Prints current date & time

# c) sys module (System-specific parameters & functions)
import sys
print(sys.version)  # Prints Python version

# ------------------------------------------------
# 16. Reloading a Module (Useful when a module is modified)
# ------------------------------------------------
import importlib
importlib.reload(mymodule)

# ------------------------------------------------
# 17. Installing External Modules using pip
# ------------------------------------------------
# Some modules are not built-in and need to be installed using `pip`.

# Example:
# pip install requests  # Installing requests module

import requests
response = requests.get("https://www.google.com")
print(response.status_code)  # Output: 200 (Success)

# ------------------------------------------------
# Summary
# ------------------------------------------------
# - **Modules** allow code reusability and better organization.
# - **Types**: Built-in (e.g., math, os) and User-defined (custom .py files).
# - **Importing**: `import module`, `from module import function`, `import module as alias`.
# - **Built-in properties**: `__name__`, `__doc__`, `dir(module)`, `module.__file__`.
# - **Packages**: Folders containing multiple modules with `__init__.py`.
# - **Using pip** to install external modules.

