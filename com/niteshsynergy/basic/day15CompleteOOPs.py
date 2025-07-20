"""
Python Object-Oriented Programming (OOP) - Complete Guide
"""

# ------------------------------------------------
# 1. Procedural v/s Object-Oriented Programming (OOP)
# ------------------------------------------------
# - **Procedural Programming**: Focuses on functions and procedures to perform operations.
# - **Object-Oriented Programming**: Focuses on data (objects) and behavior (methods).

# ------------------------------------------------
# 2. Principles of OOP
# ------------------------------------------------
# a) **Encapsulation**: Restrict direct access to some data.
# b) **Abstraction**: Hides implementation details, showing only relevant functionality.

# ------------------------------------------------
# 3. Classes and Objects
# ------------------------------------------------
# A **class** is a blueprint for creating objects.
# An **object** is an instance of a class.

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age    # Instance Variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an Object
person1 = Person("Alice", 30)
person1.display()  # Output: Name: Alice, Age: 30

# ------------------------------------------------
# 4. Types of Variables
# ------------------------------------------------
class Example:
    class_variable = "I am a class variable"  # Class Variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance Variable

# ------------------------------------------------
# 5. Types of Methods
# ------------------------------------------------
class Demo:
    class_var = "Class Variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var  # Instance Variable

    def instance_method(self):  # Works with instance
        return self.instance_var

    @classmethod
    def class_method(cls):  # Works with class
        return cls.class_var

    @staticmethod
    def static_method():  # No access to class/instance variables
        return "I am a static method"

obj = Demo("Instance Variable")
print(obj.instance_method())  # Output: Instance Variable
print(Demo.class_method())    # Output: Class Variable
print(Demo.static_method())   # Output: I am a static method

# ------------------------------------------------
# 6. Object Initialization & ‘self’ reference variable
# ------------------------------------------------
# The `self` keyword refers to the current instance of the class.

# ------------------------------------------------
# 7. ‘cls’ reference variable
# ------------------------------------------------
# The `cls` keyword is used for class methods to refer to class variables.

# ------------------------------------------------
# 8. Access Modifiers (Public, Protected, Private)
# ------------------------------------------------
class AccessModifiers:
    public_var = "Public"
    _protected_var = "Protected"
    __private_var = "Private"

    def get_private(self):
        return self.__private_var  # Can be accessed via a method

obj = AccessModifiers()
print(obj.public_var)   # Accessible
print(obj._protected_var)  # Accessible (but conventionally should not be modified)
# print(obj.__private_var)  # Error! Private variable
print(obj.get_private())  # Accessing private variable via method

# ------------------------------------------------
# 9. Property() Object
# ------------------------------------------------
class PropertyExample:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        self._value = new_value

    value = property(get_value, set_value)

obj = PropertyExample(10)
print(obj.value)  # Output: 10
obj.value = 20
print(obj.value)  # Output: 20

# ------------------------------------------------
# 10. Polymorphism (Method Overriding & Overloading)
# ------------------------------------------------
# Method Overriding (Child class modifies parent class method)
class Parent:
    def show(self):
        return "Parent Class"

class Child(Parent):
    def show(self):
        return "Child Class"

obj = Child()
print(obj.show())  # Output: Child Class

# Method Overloading (Same method, different parameters)
class OverloadExample:
    def add(self, a, b, c=0):
        return a + b + c

obj = OverloadExample()
print(obj.add(5, 10))  # Output: 15
print(obj.add(5, 10, 20))  # Output: 35

# ------------------------------------------------
# 11. Operator Overloading
# ------------------------------------------------
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

v1 = Vector(10)
v2 = Vector(20)
v3 = v1 + v2
print(v3.x)  # Output: 30

# ------------------------------------------------
# 12. Inheritance Types
# ------------------------------------------------
# a) Single Inheritance
class A:
    def method_A(self):
        return "Method in A"

class B(A):
    def method_B(self):
        return "Method in B"

obj = B()
print(obj.method_A())  # Output: Method in A

# b) Multi-level Inheritance
class C(B):
    def method_C(self):
        return "Method in C"

obj = C()
print(obj.method_A())  # Output: Method in A
print(obj.method_B())  # Output: Method in B
print(obj.method_C())  # Output: Method in C

# c) Multiple Inheritance
class X:
    def method_X(self):
        return "Method in X"

class Y:
    def method_Y(self):
        return "Method in Y"

class Z(X, Y):
    pass

obj = Z()
print(obj.method_X())  # Output: Method in X
print(obj.method_Y())  # Output: Method in Y

# ------------------------------------------------
# 13. super() - Calling Parent Class Method
# ------------------------------------------------
class Parent:
    def show(self):
        print("Parent Show Method")

class Child(Parent):
    def show(self):
        super().show()  # Calling Parent Method
        print("Child Show Method")

obj = Child()
obj.show()
# Output:
# Parent Show Method
# Child Show Method

# ------------------------------------------------
# 14. Method Resolution Order (MRO)
# ------------------------------------------------
# Determines the order in which methods are inherited.
print(Z.__mro__)  # Shows inheritance order

# ------------------------------------------------
# 15. Duck Typing (Dynamic Typing)
# ------------------------------------------------
class Duck:
    def speak(self):
        return "Quack Quack!"

class Dog:
    def speak(self):
        return "Bark!"

def make_speak(obj):
    return obj.speak()

duck = Duck()
dog = Dog()
print(make_speak(duck))  # Output: Quack Quack!
print(make_speak(dog))  # Output: Bark!

# ------------------------------------------------
# 16. Abstract Base Classes (ABC)
# ------------------------------------------------
from abc import ABC, abstractmethod

class AbstractExample(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractExample):
    def abstract_method(self):
        return "Implemented abstract method"

obj = ConcreteClass()
print(obj.abstract_method())  # Output: Implemented abstract method

# ------------------------------------------------
# 17. Inner Classes
# ------------------------------------------------
class Outer:
    class Inner:
        def display(self):
            return "Inner Class Method"

outer_obj = Outer()
inner_obj = outer_obj.Inner()
print(inner_obj.display())  # Output: Inner Class Method

# ------------------------------------------------
# Summary
# ------------------------------------------------
# - **OOP Concepts**: Classes, Objects, Encapsulation, Inheritance, Polymorphism.
# - **Access Modifiers**: Public, Protected, Private.
# - **Types of Methods**: Instance, Class, Static.
# - **Inheritance**: Single, Multi-level, Multiple.
# - **Overloading & Overriding**: Method, Constructor, Operator.
# - **Advanced OOP**: `super()`, ABC, Inner Classes.

