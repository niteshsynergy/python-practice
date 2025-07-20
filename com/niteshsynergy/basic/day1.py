# 1. Python Data Types
str="Welcome TO Python..."
print(str)
a=10
print("value of a:",a)

list=[1,"Welcome",3,2,3,4]
print("value of list:",list)

tuple=(1,"Welcome",3,1,3,45,5,-11)
print("value of tuple:",tuple)

set={1,2,3,4,3,"Welcome","Welcome","a","a","b",'a','a',5,9,10}
print("value of set:",set)

frozenset=frozenset(set)
print("value of frozenset:",frozenset)

dict={"synergy":12,"welcome":12,"apple":13,"Apple":"apple","cute":"cute","synergy":12,"welcome":12,"apple":13,"Apple":"apple","cute":"cute"}
print("value of dict:",dict)

bool=True
print("value of bool:",bool)
bool=False
print("value of bool:",bool)


bytes=101010
print("value of bytes:",bytes)
# bytearray=bytearray(bytes)
bytearray={11111,11111,111}
print("value of bytearray:",bytearray)

# memoryview=memoryview(bytearray)
memoryview=[1111,1111, 122,"Welcome"]
print("value of memoryview:",memoryview)












# 1. Python Data Types
#
# Python has several built-in data types:
# a) Numeric Types
#
#     int (Integer): Whole numbers, e.g., 10, -5
#     float (Floating point): Decimal numbers, e.g., 10.5, -3.14
#     complex (Complex numbers): e.g., 3 + 4j
#
# b) Sequence Types
#
#     str (String): Text, e.g., "hello", 'Python'
#     list (List): Ordered, mutable collection, e.g., [1, 2, 3]
#     tuple (Tuple): Ordered, immutable collection, e.g., (1, 2, 3)
#
# c) Set Types
#
#     set: Unordered, unique elements, e.g., {1, 2, 3}
#     frozenset: Immutable version of a set.
#
# d) Mapping Type
#
#     dict (Dictionary): Key-value pairs, e.g., {"name": "John", "age": 25}
#
# e) Boolean Type
#
#     bool: True or False
#
# f) Binary Types
#
#     bytes: Immutable byte sequence
#     bytearray: Mutable byte sequence
#     memoryview: Memory view object
#

