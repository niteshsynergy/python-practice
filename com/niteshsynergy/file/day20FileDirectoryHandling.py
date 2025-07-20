"""
Python File & Directory Handling - Complete Guide
"""

import os
import csv
import json
import pickle
import xml.etree.ElementTree as ET

# ------------------------------------------------
# 1. Introduction to Files
# ------------------------------------------------
"""
- A **file** is used to store data persistently on a disk.
- Python provides built-in functions to handle files easily.
- **Common File Types**:
  - Text Files (.txt, .log)
  - CSV Files (.csv)
  - JSON Files (.json)
  - Binary Files (.bin)
  - XML Files (.xml)
"""

# ------------------------------------------------
# 2. Opening a File
# ------------------------------------------------
"""
- `open(filename, mode)`: Opens a file.
- **Modes**:
  - `"r"`  → Read (default)
  - `"w"`  → Write (overwrites existing content)
  - `"a"`  → Append (adds new content)
  - `"rb"` → Read in binary mode
  - `"wb"` → Write in binary mode
  - `"r+"` → Read & Write
"""

# ------------------------------------------------
# 3. Reading Data from a File
# ------------------------------------------------
# Create a sample file for reading
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\nThis is the second line.")

# Read content from the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# ------------------------------------------------
# 4. Writing Data into a File
# ------------------------------------------------
with open("output.txt", "w") as file:
    file.write("This is a new file created using Python.\n")
    file.write("Second line added.")

print("Data written to output.txt")

# ------------------------------------------------
# 5. Appending Data into a File
# ------------------------------------------------
with open("output.txt", "a") as file:
    file.write("\nAppending this line to the file.")

print("Data appended to output.txt")

# ------------------------------------------------
# 6. Line Count in a File
# ------------------------------------------------
with open("sample.txt", "r") as file:
    line_count = len(file.readlines())

print(f"Total lines in sample.txt: {line_count}")

# ------------------------------------------------
# 7. Directory Handling - Creating, Listing, Removing Directories
# ------------------------------------------------
"""
- `os.mkdir(directory_name)`: Creates a new directory.
- `os.listdir(directory_path)`: Lists files & directories.
- `os.rmdir(directory_name)`: Removes an empty directory.
- `os.remove(file_name)`: Deletes a file.
"""

# Creating a new directory
if not os.path.exists("test_directory"):
    os.mkdir("test_directory")
    print("Directory 'test_directory' created.")

# Listing all files and directories
print("Current Directory Files:", os.listdir("."))

# Removing a file (if exists)
if os.path.exists("output.txt"):
    os.remove("output.txt")
    print("Deleted output.txt file.")

# ------------------------------------------------
# 8. CSV File Handling
# ------------------------------------------------
"""
- CSV (Comma Separated Values) is widely used in AI & data science for storing tabular data.
- The `csv` module helps read & write CSV files easily.
"""

# ------------------------------------------------
# 9. Creating & Writing into a CSV File
# ------------------------------------------------
csv_filename = "data.csv"

# Writing CSV file
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Los Angeles"])

print(f"CSV file '{csv_filename}' created.")

# ------------------------------------------------
# 10. Reading Data from a CSV File
# ------------------------------------------------
with open(csv_filename, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ------------------------------------------------
# 11. Object Serialization using Pickle Module
# ------------------------------------------------
"""
- `pickle` is used to serialize (convert objects to byte stream) and deserialize Python objects.
- Useful for **saving AI models, configurations, and preprocessed data**.
"""

data = {"name": "Alice", "age": 25, "city": "New York"}

# Saving (Pickling) the object
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Data serialized and saved as 'data.pkl'")

# Loading (Unpickling) the object
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print("Loaded Data:", loaded_data)

# ------------------------------------------------
# 12. JSON Parsing (Handling JSON Data)
# ------------------------------------------------
"""
- JSON (JavaScript Object Notation) is widely used for data exchange.
- It is essential in **AI models, APIs, and web applications**.
"""

# Creating JSON data
json_data = {"name": "John", "age": 28, "city": "San Francisco"}

# Writing JSON file
with open("data.json", "w") as file:
    json.dump(json_data, file, indent=4)

print("JSON data saved to 'data.json'")

# Reading JSON file
with open("data.json", "r") as file:
    loaded_json = json.load(file)
    print("Loaded JSON Data:", loaded_json)

# ------------------------------------------------
# 13. XML Parsing
# ------------------------------------------------
"""
- XML (Extensible Markup Language) is used in configurations, APIs, and data storage.
- `xml.etree.ElementTree` module is used for XML handling.
"""

xml_data = """<data>
    <person>
        <name>John Doe</name>
        <age>30</age>
        <city>New York</city>
    </person>
</data>"""

# Writing XML to file
with open("data.xml", "w") as file:
    file.write(xml_data)

# Parsing XML
tree = ET.parse("data.xml")
root = tree.getroot()

# Extracting data
for person in root.findall("person"):
    name = person.find("name").text
    age = person.find("age").text
    city = person.find("city").text
    print(f"XML Parsed Data: Name={name}, Age={age}, City={city}")

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **File Handling**:
  - Read, Write, Append files using `open()`.
  - Count lines in a file.
  - Manage directories using `os` module.

- **CSV File Handling**:
  - Use `csv.writer()` to write data.
  - Use `csv.reader()` to read data.

- **Object Serialization (Pickle)**:
  - `pickle.dump()` saves objects.
  - `pickle.load()` loads serialized objects.

- **JSON Parsing**:
  - `json.dump()` writes JSON files.
  - `json.load()` reads JSON files.

- **XML Parsing**:
  - Use `xml.etree.ElementTree` for parsing XML.
  - Extract XML data using `find()` and `findall()`.

- **Real-world Applications in AI**:
  - **CSV & JSON**: Storing datasets & model configurations.
  - **Pickle**: Saving trained AI models.
  - **XML**: Parsing configuration files for AI tools.
"""
