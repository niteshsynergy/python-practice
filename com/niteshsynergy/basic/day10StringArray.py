# String Basics
s = "Hello, Python!"

# Accessing Characters
print(s[0])    # First character: 'H'
print(s[-1])   # Last character: '!'

# Slicing Strings
print(s[0:5])   # 'Hello'
print(s[:5])    # 'Hello' (default start = 0)
print(s[7:])    # 'Python!' (default end = last)

# String Length
print(len(s))  # 14

# String Concatenation
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # 'Hello World'

# String Repetition
print(str1 * 3)  # 'HelloHelloHello'

# Checking Substrings
print("Python" in s)   # True
print("Java" not in s) # True

# String Methods
print(s.lower())       # 'hello, python!'
print(s.upper())       # 'HELLO, PYTHON!'
print(s.title())       # 'Hello, Python!'
print(s.capitalize())  # 'Hello, python!'
print(s.swapcase())    # 'hELLO, pYTHON!'

# Removing Whitespaces
ws = "  Hello World  "
print(ws.strip())  # 'Hello World'
print(ws.lstrip()) # 'Hello World  '
print(ws.rstrip()) # '  Hello World'

# Splitting & Joining
words = "apple,banana,grape"
print(words.split(","))  # ['apple', 'banana', 'grape']
word_list = ["Hello", "World"]
print(" ".join(word_list))  # 'Hello World'

# Replacing Strings
print(s.replace("Python", "Java"))  # 'Hello, Java!'

# String Formatting
name, age = "Alice", 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")  # f-string

# Finding & Counting
print(s.find("Python"))  # 7 (index where 'Python' starts)
print(s.count("l"))      # 2 (count occurrences of 'l')

# Checking String Types
print("hello".isalpha())  # True (only letters)
print("123".isdigit())    # True (only numbers)
print("Hello123".isalnum()) # True (letters + numbers)
print("hello".islower())  # True (all lowercase)
print("HELLO".isupper())  # True (all uppercase)
print("Hello World".istitle()) # True (title case)
print("   ".isspace())    # True (only spaces)

# Escaping Characters
print("She said, \"Hello!\"")  # She said, "Hello!"

# Multi-line Strings
multi_line = """This is
a multi-line
string."""
print(multi_line)

# String Iteration
for char in s:
    print(char, end=" ")  # H e l l o ,   P y t h o n !

# Reverse a String
print(s[::-1])  # '!nohtyP ,olleH'

# Convert to List and Back to String
char_list = list(s)
print(char_list)  # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!']
print("".join(char_list))  # 'Hello, Python!'

# Checking Start and End of Strings
print(s.startswith("Hello"))  # True
print(s.endswith("!"))        # True


# ------------------------
# STRING CONCEPTS IN PYTHON
# ------------------------

# String Basics
s = "Hello, Python!"

# Accessing Characters
print(s[0])    # 'H' (First character)
print(s[-1])   # '!' (Last character)

# Slicing Strings
print(s[0:5])   # 'Hello'
print(s[:5])    # 'Hello' (default start = 0)
print(s[7:])    # 'Python!' (default end = last)
print(s[::-1])  # Reverse string: '!nohtyP ,olleH'

# String Length
print(len(s))  # 14

# String Concatenation & Repetition
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # 'Hello World'
print(str1 * 3)  # 'HelloHelloHello'

# Checking Substrings
print("Python" in s)   # True
print("Java" not in s) # True

# String Methods
print(s.lower())       # 'hello, python!'
print(s.upper())       # 'HELLO, PYTHON!'
print(s.title())       # 'Hello, Python!'
print(s.capitalize())  # 'Hello, python!'
print(s.swapcase())    # 'hELLO, pYTHON!'

# Removing Whitespaces
ws = "  Hello World  "
print(ws.strip())  # 'Hello World'
print(ws.lstrip()) # 'Hello World  '
print(ws.rstrip()) # '  Hello World'

# Splitting & Joining
words = "apple,banana,grape"
print(words.split(","))  # ['apple', 'banana', 'grape']
word_list = ["Hello", "World"]
print(" ".join(word_list))  # 'Hello World'

# Replacing Strings
print(s.replace("Python", "Java"))  # 'Hello, Java!'

# String Formatting
name, age = "Alice", 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")  # f-string

# Finding & Counting
print(s.find("Python"))  # 7 (index where 'Python' starts)
print(s.count("l"))      # 2 (count occurrences of 'l')

# Checking String Types
print("hello".isalpha())  # True (only letters)
print("123".isdigit())    # True (only numbers)
print("Hello123".isalnum()) # True (letters + numbers)
print("hello".islower())  # True (all lowercase)
print("HELLO".isupper())  # True (all uppercase)
print("Hello World".istitle()) # True (title case)
print("   ".isspace())    # True (only spaces)

# Escaping Characters
print("She said, \"Hello!\"")  # She said, "Hello!"

# Multi-line Strings
multi_line = """This is
a multi-line
string."""
print(multi_line)

# String Iteration
for char in s:
    print(char, end=" ")  # H e l l o ,   P y t h o n !

# Convert to List and Back to String
char_list = list(s)
print(char_list)  # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'P', 'y', 't', 'h', 'o', 'n', '!']
print("".join(char_list))  # 'Hello, Python!'

# Checking Start and End of Strings
print(s.startswith("Hello"))  # True
print(s.endswith("!"))        # True


# ------------------------
# ARRAY (LIST) CONCEPTS IN PYTHON
# ------------------------

# Creating a List (Array)
arr = [10, 20, 30, 40, 50]

# Accessing Elements
print(arr[0])    # 10 (First element)
print(arr[-1])   # 50 (Last element)

# Slicing a List
print(arr[1:4])  # [20, 30, 40]
print(arr[:3])   # [10, 20, 30]
print(arr[2:])   # [30, 40, 50]
print(arr[::-1]) # [50, 40, 30, 20, 10] (Reverse list)

# Modifying Elements
arr[1] = 25
print(arr)  # [10, 25, 30, 40, 50]

# Adding Elements
arr.append(60)  # Adds 60 to the end
print(arr)  # [10, 25, 30, 40, 50, 60]

arr.insert(2, 15)  # Inserts 15 at index 2
print(arr)  # [10, 25, 15, 30, 40, 50, 60]

# Removing Elements
arr.remove(30)  # Removes first occurrence of 30
print(arr)  # [10, 25, 15, 40, 50, 60]

popped_value = arr.pop()  # Removes and returns last element
print(popped_value)  # 60
print(arr)  # [10, 25, 15, 40, 50]

# Finding Elements
print(arr.index(25))  # 1 (index of first occurrence of 25)
print(40 in arr)  # True (Checks if 40 exists)

# Counting Elements
print(arr.count(10))  # 1 (Counts occurrences of 10)

# Sorting and Reversing
arr.sort()  # Sorts in ascending order
print(arr)  # [10, 15, 25, 40, 50]

arr.reverse()  # Reverses the list
print(arr)  # [50, 40, 25, 15, 10]

# List Comprehension (Creating a new list)
squared_numbers = [x ** 2 for x in arr]
print(squared_numbers)  # [2500, 1600, 625, 225, 100]

# Iterating Over a List
for num in arr:
    print(num, end=" ")  # 50 40 25 15 10

# Copying a List
copy_list = arr.copy()
print(copy_list)  # [50, 40, 25, 15, 10]

# Clearing a List
arr.clear()
print(arr)  # []

# Nested Lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6 (Accessing row 1, column 2)

