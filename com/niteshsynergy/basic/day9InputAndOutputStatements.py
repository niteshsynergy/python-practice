name =input(("Enter Your Name"))
print(name)

age = int(input("Enter your age: "))
print(f"Next year, you will be {age + 1} years old.")

height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")

x, y = input("Enter two numbers: ").split()
print(f"First number: {x}, Second number: {y}")

a, b = map(int, input("Enter two numbers: ").split())
print(f"Sum: {a + b}")


with open("output.txt", "w") as file:
    file.write("Hello, File Handling!")


with open("output.txt", "r") as file:
    content = file.read()
    print(content)


name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

expression = input("Enter a mathematical expression: ")
result = eval(expression)
print("Result:", result)
