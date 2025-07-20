"""
Python Exception Handling - Complete Guide
"""

# ------------------------------------------------
# 1. What is an Exception?
# ------------------------------------------------
# - An **exception** is an event that disrupts the normal flow of a program.
# - It occurs during runtime when the program encounters an **error**.

# ------------------------------------------------
# 2. Why Exception Handling?
# ------------------------------------------------
# - To **prevent crashes** and handle errors gracefully.
# - To ensure a **smooth user experience**.
# - Helps in **debugging and logging errors**.

# ------------------------------------------------
# 3. Syntax Error vs Runtime Error
# ------------------------------------------------
# - **Syntax Error**: Occurs when Python fails to parse the code (before execution).
# - **Runtime Error (Exception)**: Occurs during execution due to invalid operations.

# Example of Syntax Error:
# print("Hello"  # Missing closing parenthesis (Uncomment to see error)

# Example of Runtime Error (Exception):
# print(10 / 0)  # Division by zero (ZeroDivisionError)

# ------------------------------------------------
# 4. Common Exception Types in Python
# ------------------------------------------------
"""
AttributeError - Accessing a non-existent attribute
ValueError - Invalid value passed to a function
IndexError - Accessing an out-of-range index
KeyError - Accessing a non-existent dictionary key
TypeError - Performing an operation on incompatible data types
ZeroDivisionError - Dividing by zero
FileNotFoundError - File not found error
"""

# ------------------------------------------------
# 5. Handling Exceptions - Try-Except Block
# ------------------------------------------------
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")

# ------------------------------------------------
# 6. Try with Multiple Except Blocks
# ------------------------------------------------
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
except IndexError:
    print("Error: Index out of range!")
except Exception as e:
    print(f"General Exception: {e}")

# ------------------------------------------------
# 7. Handling Multiple Exceptions with a Single Except Block
# ------------------------------------------------
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except (ZeroDivisionError, ValueError) as e:
    print(f"Exception Occurred: {e}")

# ------------------------------------------------
# 8. Finally Block
# ------------------------------------------------
# The `finally` block executes whether an exception occurs or not.

try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing resources...")

# ------------------------------------------------
# 9. Try-Except-Finally Example
# ------------------------------------------------
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error!")
finally:
    print("This always runs.")  # Executes no matter what

# ------------------------------------------------
# 10. Raising Exceptions - The `raise` Keyword
# ------------------------------------------------
# `raise` is used to throw exceptions intentionally.

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18!")
    return "Access Granted"

try:
    print(check_age(16))
except ValueError as e:
    print(f"Custom Exception: {e}")

# ------------------------------------------------
# 11. Custom (User-Defined) Exceptions
# ------------------------------------------------
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in account!"):
        self.message = message
        super().__init__(self.message)

try:
    raise InsufficientFundsError()
except InsufficientFundsError as e:
    print(f"Custom Error Caught: {e}")

# ------------------------------------------------
# 12. Banking System Example (Real-Life Exception Handling)
# ------------------------------------------------

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw ₹{amount}. Available balance: ₹{self.balance}")
        self.balance -= amount
        print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")

    def transfer(self, recipient, amount):
        try:
            self.withdraw(amount)
            recipient.deposit(amount)
            print(f"Transferred ₹{amount} to account {recipient.account_number}")
        except InsufficientFundsError as e:
            print(f"Transfer Failed: {e}")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: ₹{self.balance}")

# Creating bank accounts
acc1 = BankAccount("A123", 5000)
acc2 = BankAccount("B456", 2000)

# Performing Transactions with Exception Handling
try:
    acc1.deposit(1000)
    acc1.withdraw(2000)
    acc1.transfer(acc2, 5000)  # This will trigger an InsufficientFundsError
except (ValueError, InsufficientFundsError) as e:
    print(f"Transaction Error: {e}")

# Display final balances
acc1.display_balance()
acc2.display_balance()

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **Exceptions**: Errors that occur at runtime.
- **Why Handle Exceptions?** To prevent crashes and ensure smooth execution.
- **Syntax Error vs Runtime Error**:
  - Syntax Error → Incorrect code structure.
  - Runtime Error (Exception) → Error during execution.
- **Common Exceptions**: ZeroDivisionError, TypeError, ValueError, etc.
- **Try-Except**: Handles exceptions.
- **Multiple Except Blocks**: Catch different exceptions separately.
- **Single Except for Multiple Errors**: `(ZeroDivisionError, ValueError)`
- **Finally Block**: Always executes.
- **raise**: Manually raises exceptions.
- **Custom Exceptions**: Define user-specific errors.
- **Banking System Example**: Demonstrates real-world use of exception handling.
"""
