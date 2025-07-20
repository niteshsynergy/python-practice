"""
Python Regular Expressions (RegEx) - Complete Guide
"""

import re

# ------------------------------------------------
# 1. Understanding Regular Expressions (RegEx)
# ------------------------------------------------
# - Regular expressions are used to **search, match, and manipulate text**.
# - They help in **pattern-based string processing**.

# ------------------------------------------------
# 2. String vs Regular Expression String
# ------------------------------------------------
# - A normal string is a sequence of characters.
# - A **RegEx string** contains patterns to match specific sequences.

# Example:
normal_string = "Hello123"
regex_string = r"\d+"  # Matches any digits

# ------------------------------------------------
# 3. "re" Module Functions
# ------------------------------------------------
# Python provides the `re` module to work with regular expressions.

# ------------------------------------------------
# 4. Match() - Checks for a match at the **beginning** of a string
# ------------------------------------------------
pattern = r"\d+"  # Matches digits
text = "123Hello"

match_result = re.match(pattern, text)
if match_result:
    print("Match Found:", match_result.group())  # Output: 123

# ------------------------------------------------
# 5. Search() - Finds the **first occurrence** of a pattern in a string
# ------------------------------------------------
text = "Hello 123, Welcome 456"
search_result = re.search(r"\d+", text)
if search_result:
    print("Search Found:", search_result.group())  # Output: 123

# ------------------------------------------------
# 6. Split() - Splits the string at each match
# ------------------------------------------------
text = "apple123banana456cherry"
split_result = re.split(r"\d+", text)
print("Split Result:", split_result)  # Output: ['apple', 'banana', 'cherry']

# ------------------------------------------------
# 7. Findall() - Returns **all matches** in a list
# ------------------------------------------------
text = "Price: $40, Discount: $10, Total: $30"
findall_result = re.findall(r"\d+", text)
print("Findall Result:", findall_result)  # Output: ['40', '10', '30']

# ------------------------------------------------
# 8. Compile() - Precompiles a pattern for reuse
# ------------------------------------------------
pattern = re.compile(r"\d+")
print(pattern.findall("123ABC456"))  # Output: ['123', '456']

# ------------------------------------------------
# 9. Sub() - Replaces all occurrences of a pattern
# ------------------------------------------------
text = "Hello123, Welcome456"
sub_result = re.sub(r"\d+", "###", text)
print("Substituted String:", sub_result)  # Output: Hello###, Welcome###

# ------------------------------------------------
# 10. Subn() - Replaces and returns the count of replacements
# ------------------------------------------------
text = "I have 2 apples and 3 bananas"
subn_result = re.subn(r"\d+", "X", text)
print("Substituted String with Count:", subn_result)  # Output: ('I have X apples and X bananas', 2)

# ------------------------------------------------
# 11. Expressions using Operators & Symbols
# ------------------------------------------------
"""
.  - Matches any character except newline
^  - Matches the start of a string
$  - Matches the end of a string
*  - Matches 0 or more repetitions
+  - Matches 1 or more repetitions
?  - Matches 0 or 1 repetition
{n} - Matches exactly n repetitions
[a-z] - Matches any lowercase letter
[A-Z] - Matches any uppercase letter
\d - Matches a digit (0-9)
\D - Matches a non-digit
\s - Matches a whitespace
\w - Matches an alphanumeric character (a-z, A-Z, 0-9, _)
"""

# ------------------------------------------------
# 12. Simple Character Matches
# ------------------------------------------------
print(re.findall(r"cat", "The cat is sitting on the mat"))  # Output: ['cat']

# ------------------------------------------------
# 13. Special Characters
# ------------------------------------------------
print(re.findall(r"\d+", "Order 3 apples and 4 bananas"))  # Output: ['3', '4']

# ------------------------------------------------
# 14. Character Classes
# ------------------------------------------------
print(re.findall(r"[aeiou]", "Hello World"))  # Output: ['e', 'o', 'o']

# ------------------------------------------------
# 15. Mobile Number Extraction
# ------------------------------------------------
text = "Call me at 9876543210 or 98765-43210"
mobile_pattern = r"\b\d{10}\b|\b\d{5}-\d{5}\b"
print("Extracted Numbers:", re.findall(mobile_pattern, text))  # Output: ['9876543210', '98765-43210']

# ------------------------------------------------
# 16. Email Extraction
# ------------------------------------------------
text = "Emails: user@example.com, test123@domain.org"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
print("Extracted Emails:", re.findall(email_pattern, text))  # Output: ['user@example.com', 'test123@domain.org']

# ------------------------------------------------
# 17. Different Email ID Patterns
# ------------------------------------------------
emails = ["abc@example.com", "123.user@domain.in", "user-name@site.net"]
for email in emails:
    print(f"{email}: {'Valid' if re.match(email_pattern, email) else 'Invalid'}")

# ------------------------------------------------
# 18. Data Extraction (Dates)
# ------------------------------------------------
text = "Meeting dates: 12/12/2023, 15-11-2022"
date_pattern = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"
print("Extracted Dates:", re.findall(date_pattern, text))  # Output: ['12/12/2023', '15-11-2022']

# ------------------------------------------------
# 19. Password Extraction (Secure Password Validation)
# ------------------------------------------------
passwords = ["Hello123", "Password!", "Abc@1234"]
password_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

for password in passwords:
    print(f"{password}: {'Valid' if re.match(password_pattern, password) else 'Invalid'}")

# ------------------------------------------------
# 20. URL Extraction
# ------------------------------------------------
text = "Visit https://www.google.com or http://example.org"
url_pattern = r"https?://[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+"
print("Extracted URLs:", re.findall(url_pattern, text))  # Output: ['https://www.google.com', 'http://example.org']

# ------------------------------------------------
# 21. Vehicle Number Extraction (India Format)
# ------------------------------------------------
text = "Vehicle numbers: MH12AB1234, KA01CD5678"
vehicle_pattern = r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}"
print("Extracted Vehicle Numbers:", re.findall(vehicle_pattern, text))  # Output: ['MH12AB1234', 'KA01CD5678']

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **RegEx Basics**: Pattern matching using `re` module.
- **Common Functions**:
  - `match()`, `search()`, `findall()`, `split()`, `sub()`, `subn()`.
- **Character Classes & Special Characters**: `[a-z]`, `\d`, `\s`, `\w`.
- **Practical Applications**:
  - **Extracting Phone Numbers**
  - **Extracting Emails & URLs**
  - **Validating Passwords**
  - **Extracting Dates & Vehicle Numbers**
"""
