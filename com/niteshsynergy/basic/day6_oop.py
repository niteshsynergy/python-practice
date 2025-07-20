# Example: Creating a Class and Object
class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def printCar(self):
        print(self.brand,self.model)

    def display_info(self):
        return f"car is {self.brand} {self.model}"

# create car object
carObj = Car("NiteshSynery","S23")
print("Hii")
print(carObj.display_info())
print("Hii")
carObj.printCar()

# Example: Public, Protected, and Private Variables
# Encapsulation Benefits:
    # Prevents direct modification of sensitive data.
    # Controls access using getter and setter methods.
class Person:
    def __init__(self,name,age):
        self.name = name # Public attribute
        self._age = age # Protected  attribute
        self.__salary = 1000 # Private attribute


    def get_salary(self):
        return self.__salary

person=Person("Rahul",19)
print(person.name)
print(person.get_salary())

print(person._age)
# print(p.__salary)  # Error: AttributeError
print(person.get_salary())  # Correct way to access private data




# Example: Using Abstract Base Class (ABC)
# Abstraction Benefits:
#
#     Enforces a standard interface across different implementations.
#     Hides complex logic and provides only relevant details.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass




class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


dog = Dog()
print(dog.sound())
cat = Cat()
print(cat.sound())




# 🔹 4. Inheritance
# Example: Single Inheritance

class  Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def show_brand(self):
        return f"Brand is {self.brand}"

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model


    def show_details(self):
        return f"Car is {self.brand} {self.model}"


car = Car("NiteshSynery","S24")
print(car.show_details())


# Example: Multiple Inheritance


class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def rotate(self):
        return "Wheels rotating"

class Car(Engine,Wheels):
    pass

my_car = Car()
print(my_car.start())
print(my_car.rotate())



# To check the Method Resolution Order (MRO):

# print(my_car.__mro__)

# (<class '__main__.Car'>, <class '__main__.Engine'>, <class '__main__.Wheels'>, <class 'object'>)


# 🔹 5. Polymorphism
# Example: Method Overriding
class Bird:
    def sound(self):
        return "Bird makes a sound"

class Sparrow(Bird):
    def sound(self):
        return "Chirp Chirp"

b = Bird()
s = Sparrow()
print(b.sound())
print(s.sound())

# Example: Operator Overloading

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

p1=Point(1,2)
p2=Point(3,4)
result = p1+p2
print(result.x,result.y)


# 🔹 6. Special Methods (__methods__)

# Example: __str__() and __repr__()
# Key Takeaways
#
#     __str__() is used for a user-friendly string representation (print(obj)).
#     __repr__() is used for a developer-friendly representation (repr(obj), debugging).
#     If __str__() is missing, Python defaults to __repr__().
#     Useful for logging, debugging, and printing objects correctly.
# Python provides dunder (double underscore) methods for special behavior.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person is {self.name} {self.age} years old"

    def __repr__(self):
        return f"Person is {self.name} {self.age} years old"

p=Person("Rahul",19)

print(p.__str__())
print(p.__repr__())
print(str(p))
print(repr(p))



# Static Methods and Class Methods

class MathOperations:
    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def sub(cls,a,b): # Uses cls (class reference)
        return a-b

print(MathOperations.add(10,20))
mo = MathOperations()
print(mo.sub(12,10))


# Metaclasses
# Provides flexibility and customization.
# Allows meta-programming techniques


class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['greet'] = lambda self: f"Hello from {name}"
        return super().__new__(cls, name, bases, dct)

class Test(metaclass=Meta):
    pass

t = Test()
print(t.greet())  # Output: Hello from Test











#
# Object-Oriented Programming (OOP) in Python
# 1. Properties of a Class in Python
#
# A class in Python consists of the following properties:
#
#     Encapsulation: Bundling data and methods that operate on the data into a single unit (class).
#     Abstraction: Hiding the internal implementation details and exposing only necessary functionality.
#     Inheritance: A mechanism that allows one class to derive properties and methods from another class.
#     Polymorphism: The ability of different objects to be treated as instances of the same class through a common interface.
#
# 2. Rules & Guidelines for Classes and Objects
# Class Rules:
#
#     Class names should follow PascalCase (e.g., EmployeeDetails).
#     Class definitions start with the class keyword.
#     A class can contain variables (attributes) and methods (functions).
#     The __init__ method (constructor) is used to initialize objects.
#     Instance methods should have self as the first parameter.
#
# Object Rules:
#
#     Objects are created using the class name (obj = ClassName()).
#     Objects access class attributes using self.attribute.
#     Objects can call methods using obj.method_name().
#     Objects store instance-specific data.
#
# Best Practices:
#
#     Keep class methods self-contained (avoid modifying global state).
#     Use private (__var) and protected (_var) attributes where necessary.
#     Implement getter and setter methods instead of directly modifying attributes.
#
# 3. Summary of Key OOP Concepts
# Concept	Description
# Class	A blueprint for creating objects (e.g., class Car:).
# Object	An instance of a class with specific attributes and methods.
# Encapsulation	Restricting direct access to class data.
# Abstraction	Hiding complex implementation details and exposing essential features.
# Inheritance	A class derives attributes and behavior from another class.
# Polymorphism	The ability of different objects to use a common interface.
# 4. Topics Breakdown
#
# Below is a structured way to cover each topic in depth:
# 🔹 Basics of Class and Object
#
#     Defining a class
#     Creating an object
#     Understanding the __init__ constructor
#
# 🔹 Encapsulation
#
#     Public, protected, and private variables
#     Getter and setter methods
#     Property decorators (@property)
#
# 🔹 Abstraction
#
#     Hiding details using abstract classes
#     Using ABC (Abstract Base Class)
#
# 🔹 Inheritance
#
#     Single and multiple inheritance
#     Overriding parent class methods
#     super() function
#
# 🔹 Polymorphism
#
#     Method Overriding
#     Operator Overloading
#     Duck Typing
#
# 🔹 Special Methods in Python (__methods__)
#
#     __str__() for string representation
#     __repr__() for official string representation
#     __eq__() for comparing objects
#
# 🔹 Advanced OOP Concepts
#
#     Metaclasses
#     Class decorators
#     Static methods and class methods
#
