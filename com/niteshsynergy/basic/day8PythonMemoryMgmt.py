

# 🔹 Example: Reference Counting

import sys

a = [1, 2, 3]  # Creating an object
b = a  # Reference count increases
c = a  # Reference count increases

print(sys.getrefcount(a))  # Output: 4 (Includes function stack reference)

del b  # Reference count decreases
del c  # Reference count decreases

print(sys.getrefcount(a))  # Output: 2 (1 from the function stack and 1 from `a`)


# 3️⃣ Garbage Collection (GC)

# Since reference cycles can lead to memory leaks, Python’s Garbage Collector (GC) handles cyclic references.


import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()

a.ref = b  # a → b
b.ref = a  # b → a (Cyclic reference)

del a
del b

gc.collect()  # Manually trigger garbage collection
#
# ✅ Best Practice:
#
#     Use gc.collect() only when necessary (not frequently).
#     Use weak references (weakref module) to avoid cycles.




# 4️⃣ Python Memory Optimization Techniques


# 🔹 1. Use Generators Instead of Lists

# Lists consume more memory as they store all elements in memory at once, whereas generators yield elements on demand.


import sys

# List stores all values at once
list_nums = [i for i in range(1000000)]
print(sys.getsizeof(list_nums))  # Large memory usage

# Generator yields values one by one
gen_nums = (i for i in range(1000000))
print(sys.getsizeof(gen_nums))  # Much smaller memory footprint

# ✅ Use case: When handling large datasets, always prefer generators (yield).


# 🔹 2. Use __slots__ to Reduce Object Overhead

# By default, Python objects use dynamic dictionaries (__dict__) for attributes, which adds memory overhead. Using __slots__ restricts attributes and reduces memory consumption.

class WithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class WithSlots:
    __slots__ = ['name', 'age']  # Restricts attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age

w1 = WithoutSlots("John", 30)
w2 = WithSlots("John", 30)

import sys
print(sys.getsizeof(w1))  # Larger memory usage
print(sys.getsizeof(w2))  # Smaller memory usage




# 🔹 3. Use del and Context Managers

# Explicitly deleting objects and using context managers (with) can help release memory sooner.

import time

class LargeObject:
    def __init__(self):
        self.data = [0] * 10**6  # 1 million integers

obj = LargeObject()
del obj  # Frees memory immediately

# ✅ Use case: del is useful for large objects that are no longer needed.


# 🔹 4. Use weakref for Large Objects

# Python’s weakref module allows objects to be referenced without preventing garbage collection.

import weakref

class Data:
    pass

obj = Data()
weak_ref = weakref.ref(obj)

print(weak_ref())  # Output: <__main__.Data object>
del obj  # Original object is deleted
print(weak_ref())  # Output: None (object is garbage collected)


# 🔹 5. Optimize Large Lists Using array

# The built-in array module uses less memory compared to lists for numerical data.
import array

nums_list = [1, 2, 3, 4, 5]  # List (more memory)
nums_array = array.array('i', [1, 2, 3, 4, 5])  # Integer array (less memory)

print(nums_list.__sizeof__())  # Larger
print(nums_array.__sizeof__())  # Smaller

# ✅ Use case: When dealing with large numerical datasets.

# 🔹 6. Pooling for Frequent Objects

# Python reuses small integers (-5 to 256) and strings to save memory.

a = 256
b = 256
print(a is b)  # True (same memory location)

c = 257
d = 257
print(c is d)  # False (different memory locations)

# ✅ Use case: Avoid unnecessary object creation for frequently used values.


#
# Performance Optimization Techniques
# 🔹 1. Use Efficient String Concatenation
#
# Using + for string concatenation creates multiple intermediate strings. Use join() instead.
words = ["Python", "is", "fast"]
sentence = " ".join(words)  # Faster than using +
# ✅ Use case: Always use .join() for efficient string handling.


#
# 2. Use lru_cache for Expensive Function Calls
#
# The functools.lru_cache() stores results of expensive function calls to speed up performance.


from functools import lru_cache

@lru_cache(maxsize=100)
def slow_function(n):
    print(f"Computing {n}...")
    return n * n

print(slow_function(10))  # First call: Computed
print(slow_function(10))  # Second call: Cached result


# ✅ Use case: Optimizes repetitive function calls.

#
#  3. Use Multithreading and Multiprocessing
#
# Python has Global Interpreter Lock (GIL), which restricts multithreading for CPU-bound tasks. Use multiprocessing for CPU tasks and multithreading for I/O tasks.
#


from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as p:
    print(p.map(square, [1, 2, 3, 4, 5]))  # Parallel processing

# ✅ Use case: Use multiprocessing for CPU-intensive tasks.












# Python Memory Management Overview
# 🔹 Key Components
# Component	Description
# Stack Memory	Stores function calls and local variables.
# Heap Memory	Stores objects and dynamic allocations.
# Reference Counting	Tracks the number of references to an object.
# Garbage Collection (GC)	Removes objects that are no longer in use.
# Memory Pools (PyMalloc)	Python uses a private heap for small object allocations.
