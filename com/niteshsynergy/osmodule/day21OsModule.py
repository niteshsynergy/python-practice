"""
Python OS Module - Complete Guide
"""

import os
import shutil
import time
import platform
import subprocess

# ------------------------------------------------
# 1. Introduction to OS Module
# ------------------------------------------------
"""
- The `os` module provides a way to interact with the **operating system**.
- It allows managing files, directories, executing system commands, and more.
- Used for **automation, system administration, and file handling**.
"""

# ------------------------------------------------
# 2. Shell Script Commands using Python
# ------------------------------------------------
"""
- Python can execute **shell commands** using `os.system()` and `subprocess.run()`.
- Useful for **automation, server management, and executing scripts**.
"""

# Running a shell command
print("Current User:", os.system("whoami"))  # Linux/Mac
# os.system("dir")  # Windows

# ------------------------------------------------
# 3. Various OS Operations in Python
# ------------------------------------------------
"""
- `os.name` → Returns the name of the OS.
- `os.getcwd()` → Gets the current working directory.
- `os.listdir(path)` → Lists files and directories in a given path.
- `os.environ` → Accesses environment variables.
"""

print("OS Name:", os.name)
print("Current Working Directory:", os.getcwd())
print("Files in Directory:", os.listdir("."))

# ------------------------------------------------
# 4. Python File System Shell Methods
# ------------------------------------------------
"""
- `os.mkdir(path)` → Creates a new directory.
- `os.makedirs(path)` → Creates directories recursively.
- `os.rmdir(path)` → Removes an empty directory.
- `shutil.rmtree(path)` → Deletes a directory and its contents.
"""

# Creating a directory
dir_name = "test_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")

# Listing files after creating a directory
print("Updated Directory List:", os.listdir("."))

# Removing the directory
if os.path.exists(dir_name):
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")

# ------------------------------------------------
# 5. Creating Files and Directories
# ------------------------------------------------
"""
- `open(file, "w")` → Creates a new file.
- `os.mkdir("dir_name")` → Creates a directory.
- `os.makedirs("parent/child")` → Creates nested directories.
"""

# Creating a new file
file_name = "test_file.txt"
with open(file_name, "w") as file:
    file.write("This is a test file.")

print(f"File '{file_name}' created.")

# Creating nested directories
nested_dir = "parent_dir/child_dir"
os.makedirs(nested_dir, exist_ok=True)
print(f"Nested directory '{nested_dir}' created.")

# ------------------------------------------------
# 6. Removing Files and Directories
# ------------------------------------------------
"""
- `os.remove(file_name)` → Deletes a file.
- `shutil.rmtree(directory)` → Deletes a directory with contents.
"""

# Deleting a file
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' deleted.")

# Deleting a directory with contents
if os.path.exists("parent_dir"):
    shutil.rmtree("parent_dir")
    print("Parent directory and subdirectories deleted.")

# ------------------------------------------------
# 7. Shutdown and Restart System
# ------------------------------------------------
"""
- Shutdown & restart system (Requires Admin privileges).
- **Windows**: `os.system("shutdown /s /t 5")`  # Shutdown in 5 sec
- **Linux/Mac**: `os.system("shutdown -h now")`  # Shutdown immediately
"""

# Uncomment below commands to restart/shutdown system
# os.system("shutdown /r /t 10")  # Restart in 10 sec (Windows)
# os.system("shutdown -r now")  # Restart immediately (Linux/Mac)

# ------------------------------------------------
# 8. Renaming Files and Directories
# ------------------------------------------------
"""
- `os.rename(old_name, new_name)` → Renames a file or directory.
"""

# Creating a file to rename
with open("old_file.txt", "w") as file:
    file.write("Renaming this file.")

# Renaming the file
os.rename("old_file.txt", "new_file.txt")
print("File renamed to 'new_file.txt'.")

# Renaming a directory
os.mkdir("old_folder")
os.rename("old_folder", "new_folder")
print("Directory renamed to 'new_folder'.")

# Removing the renamed directory
os.rmdir("new_folder")

# ------------------------------------------------
# 9. Executing System Commands
# ------------------------------------------------
"""
- `os.system(command)` → Executes a command in the system shell.
- `subprocess.run(command, shell=True)` → Executes commands and returns output.
"""

# Running a system command using `os.system()`
os.system("echo Hello, OS Module!")

# Running a command using `subprocess`
output = subprocess.run("echo Hello, World!", shell=True, capture_output=True, text=True)
print("Subprocess Output:", output.stdout)

# ------------------------------------------------
# 10. Case Study - System Cleanup Script
# ------------------------------------------------
"""
- A script that **automatically cleans up temp files** and **removes old logs**.
"""


def system_cleanup():
    temp_files = ["old_log.txt", "temp_data.tmp", "cache.txt"]

    # Creating sample files for deletion
    for file in temp_files:
        with open(file, "w") as f:
            f.write("This is a temp file.")

    # Deleting temporary files
    for file in temp_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted {file}")

    print("System cleanup completed.")


# Running system cleanup
system_cleanup()

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **OS Module Basics**:
  - `os.getcwd()` → Get current directory.
  - `os.listdir(path)` → List files in a directory.
  - `os.environ` → Access system environment variables.

- **File & Directory Handling**:
  - `os.mkdir()` → Create directory.
  - `os.remove()` → Delete a file.
  - `os.rename()` → Rename files & directories.

- **System Commands**:
  - `os.system()` → Execute shell commands.
  - `subprocess.run()` → Run system commands with output capture.

- **Shutdown & Restart**:
  - Windows: `shutdown /s /t 10`
  - Linux/Mac: `shutdown -h now`

- **Real-world Applications**:
  - **System Cleanup** → Deleting temp files.
  - **Automation** → Managing directories dynamically.
  - **Executing Shell Commands** → Running scripts remotely.
"""
