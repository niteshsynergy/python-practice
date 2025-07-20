"""
Python Data Structures & Algorithms (DSA)
"""

# ---------------------------------
#  LIST COLLECTION
# ---------------------------------

# What is List?
# A list is a collection in Python that is ordered and changeable (mutable).
# It allows duplicate elements.

# Need of List collection:
# Lists are useful when you need to store a collection of related items, such as names, numbers, or objects.

# Different ways of creating a List
list1 = [1, 2, 3, 4, 5]  # List with integers
list2 = ["apple", "banana", "cherry"]  # List with strings
list3 = list(range(5))  # List from range function [0,1,2,3,4]
list4 = list("Hello")  # List from a string ['H', 'e', 'l', 'l', 'o']

# List comprehension (Creating lists in a compact way)
squares = [x ** 2 for x in range(5)]  # Output: [0, 1, 4, 9, 16]

# List indices (Accessing elements)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First element: apple
print(fruits[-1])  # Last element: cherry

# Processing elements of List through Indexing and Slicing
print(fruits[1:3])  # Slicing from index 1 to 2 (['banana', 'cherry'])
print(fruits[:2])  # First two elements

# List object methods
fruits.append("orange")  # Adds element
fruits.remove("banana")  # Removes element
fruits.insert(1, "kiwi")  # Insert at index 1
print(fruits)  # ['apple', 'kiwi', 'cherry', 'orange']

# List is Mutable (Can be modified)
fruits[0] = "mango"
print(fruits)  # ['mango', 'kiwi', 'cherry', 'orange']

# Mutable and Immutable elements of List
list_mutable = [10, [20, 30], 40]  # List containing mutable (list) and immutable (int)
list_mutable[1][0] = 25  # Changing nested list
print(list_mutable)  # Output: [10, [25, 30], 40]

# Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Output: 6

# List_of_lists
list_of_lists = [list1, list2, list3]  # List containing lists
print(list_of_lists)

# Hardcopy, ShallowCopy and DeepCopy
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

original_list[0][0] = 100
print(shallow_copy)  # Changes in nested list affect shallow copy
print(deep_copy)  # Deep copy remains unchanged

# zip() in Python (Combining lists)
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
zipped = list(zip(list_a, list_b))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# How to unzip?
unzipped = list(zip(*zipped))
print(unzipped)

# Python Arrays (Use list as an array in Python)
import array
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates integer array

# ---------------------------------
#  TUPLE COLLECTION
# ---------------------------------

# What is Tuple?
# A tuple is an immutable (unchangeable) ordered collection.

# Different ways of creating Tuple
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
tuple3 = tuple([1, 2, 3])  # Using tuple constructor

# Method of Tuple object
print(tuple1.count(2))  # Count occurrences
print(tuple1.index(3))  # Get index of element

# Tuple is Immutable
# tuple1[0] = 10  # Error!

# Mutable and Immutable elements of Tuple
tuple_with_list = (1, [2, 3], 4)
tuple_with_list[1][0] = 99  # Allowed
print(tuple_with_list)  # (1, [99, 3], 4)

# List v/s Tuple
# Lists are mutable, tuples are immutable (use tuples when data should not change)

# ---------------------------------
#  SET COLLECTION
# ---------------------------------

# What is Set?
# A set is an unordered collection with unique elements.

# Different ways of creating a Set
set1 = {1, 2, 3, 4, 5}
set2 = set([1, 2, 3, 4, 5])  # Using set constructor

# Difference between list and set
# Lists allow duplicates, sets do not

# Python Set Methods
set1.add(6)  # Adds element
set1.remove(3)  # Removes element

# Python Set Operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Union
print(A & B)  # Intersection

# Python Frozen set (Immutable Set)
frozen_set = frozenset([1, 2, 3])
# frozen_set.add(4)  # Error!

# ---------------------------------
#  DICTIONARY COLLECTION
# ---------------------------------

# What is Dictionary?
# A dictionary is an unordered collection of key-value pairs.

# Difference between list, set, and dictionary
# List: Ordered, mutable, allows duplicates
# Set: Unordered, mutable, no duplicates
# Dictionary: Key-value pairs, keys must be unique

# How to create a dictionary?
dict1 = {"name": "Alice", "age": 25, "city": "New York"}
dict2 = dict(name="Bob", age=30)

# PYTHON HASHING?
# Keys in dictionaries are hashed for fast lookup.

# Accessing values of dictionary
print(dict1["name"])  # Output: Alice
print(dict1.get("age"))  # Output: 25

# Python Dictionary Methods
dict1.update({"country": "USA"})  # Adding new key-value
del dict1["age"]  # Deleting key

# Copying dictionary
dict_copy = dict1.copy()

# Reading keys, values, items
print(dict1.keys())  # dict_keys(['name', 'city', 'country'])
print(dict1.values())  # dict_values(['Alice', 'New York', 'USA'])
print(dict1.items())  # dict_items([('name', 'Alice'), ('city', 'New York'), ('country', 'USA')])

# Sorting the Dictionary
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)

# Dictionary comprehension
squared_dict = {x: x ** 2 for x in range(5)}
print(squared_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
