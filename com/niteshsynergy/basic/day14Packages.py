"""
Python Packages - Complete Guide
"""

# ------------------------------------------------
# 1. Organizing Python Project into Packages
# ------------------------------------------------
# A **package** is a collection of modules grouped together in a directory.
# It helps in organizing large projects by structuring related modules together.

# ------------------------------------------------
# 2. Types of Packages
# ------------------------------------------------
# a) **Predefined (Built-in) Packages**: Provided by Python, e.g., `os`, `sys`, `math`.
# b) **User-defined Packages**: Custom packages created by users.

# ------------------------------------------------
# 3. Package vs Folder
# ------------------------------------------------
# - A **folder** is just a directory, but a **package** contains an `__init__.py` file.
# - The `__init__.py` file makes Python treat a folder as a package.

# Example:
"""
my_package/                # This is a package (contains __init__.py)
    __init__.py            # Marks the directory as a package
    module1.py             # First module
    module2.py             # Second module
"""

# ------------------------------------------------
# 4. Creating a Package
# ------------------------------------------------
# Create a folder `my_package/` and add an `__init__.py` file inside it.

"""
# my_package/__init__.py
# This can be empty or contain initialization code
"""

"""
# my_package/module1.py
def function1():
    return "This is function1 from module1"
"""

"""
# my_package/module2.py
def function2():
    return "This is function2 from module2"
"""

# ------------------------------------------------
# 5. Importing a Package
# ------------------------------------------------
# Importing the entire module
import my_package.module1
print(my_package.module1.function1())  # Output: This is function1 from module1

# Importing specific functions
from my_package.module2 import function2
print(function2())  # Output: This is function2 from module2

# ------------------------------------------------
# 6. Importing All Modules from a Package
# ------------------------------------------------
# Modify `__init__.py` in `my_package/` to include:
"""
# my_package/__init__.py
from .module1 import function1
from .module2 import function2
"""

# Now, we can import directly:
from my_package import function1, function2
print(function1())  # Output: This is function1 from module1
print(function2())  # Output: This is function2 from module2

# ------------------------------------------------
# 7. Understanding PIP (Python Package Installer)
# ------------------------------------------------
# - PIP is a package manager for Python that allows installing third-party packages.
# - It simplifies package installation, updating, and removal.

# ------------------------------------------------
# 8. Installing PIP (If not already installed)
# ------------------------------------------------
# Check if PIP is installed:
"""
pip --version
"""

# If not installed, install using:
"""
python -m ensurepip --default-pip
"""

# ------------------------------------------------
# 9. Installing Python Packages Using PIP
# ------------------------------------------------
# Syntax:
"""
pip install package_name
"""

# Example: Install `requests` package
"""
pip install requests
"""

# ------------------------------------------------
# 10. Listing Installed Packages
# ------------------------------------------------
"""
pip list
"""

# ------------------------------------------------
# 11. Checking Package Information
# ------------------------------------------------
"""
pip show package_name
"""

# Example:
"""
pip show requests
"""

# ------------------------------------------------
# 12. Upgrading a Package
# ------------------------------------------------
"""
pip install --upgrade package_name
"""

# Example:
"""
pip install --upgrade requests
"""

# ------------------------------------------------
# 13. Uninstalling a Package
# ------------------------------------------------
"""
pip uninstall package_name
"""

# Example:
"""
pip uninstall requests
"""

# ------------------------------------------------
# Summary
# ------------------------------------------------
# - **Packages** organize Python projects by grouping related modules.
# - **Folder vs Package**: A package contains `__init__.py`, a folder does not.
# - **Importing a package**: `import package.module`, `from package import module`.
# - **PIP**: Python's package manager for installing third-party packages.
# - **Common PIP commands**:
#   - `pip install package_name`
#   - `pip uninstall package_name`
#   - `pip list` (view installed packages)
#   - `pip show package_name` (view package details)
#   - `pip install --upgrade package_name` (upgrade package)
