"""
Python Logging & Date-Time Module - Complete Guide
"""

import logging
import datetime
import time
import calendar

# ------------------------------------------------
# 1. Logging Levels in Python
# ------------------------------------------------
"""
DEBUG - Detailed diagnostic information.
INFO - Confirmation that things are working as expected.
WARNING - Indication of potential issues.
ERROR - Due to a more serious problem.
CRITICAL - A very serious error.
"""

# ------------------------------------------------
# 2. Implement Logging (Basic Configuration)
# ------------------------------------------------
logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a Debug message")
logging.info("This is an Info message")
logging.warning("This is a Warning message")
logging.error("This is an Error message")
logging.critical("This is a Critical message")

# ------------------------------------------------
# 3. Configure Log File in Overwriting Mode
# ------------------------------------------------
logging.basicConfig(filename="app.log", filemode="w", level=logging.DEBUG)
logging.info("This will be written to app.log in overwrite mode")

# ------------------------------------------------
# 4. Adding Timestamp in the Log Messages
# ------------------------------------------------
logging.basicConfig(
    filename="app_timestamp.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
logging.info("Timestamp is added to the log messages")

# ------------------------------------------------
# 5. Python Program Exceptions to the Log File
# ------------------------------------------------
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Exception occurred: %s", e)

# ------------------------------------------------
# 6. Custom Logger (Requirement of Customized Logger)
# ------------------------------------------------
# Sometimes, we need a more flexible logging setup.

# ------------------------------------------------
# 7. Features of a Customized Logger
# ------------------------------------------------
"""
- Multiple log handlers (console & file)
- Different log levels for different handlers
- Custom log formatting
"""

# Creating a Customized Logger
custom_logger = logging.getLogger("MyLogger")
custom_logger.setLevel(logging.DEBUG)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# File Handler
file_handler = logging.FileHandler("custom_logger.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Adding Handlers to Logger
custom_logger.addHandler(console_handler)
custom_logger.addHandler(file_handler)

# Logging Messages
custom_logger.debug("Debug message")
custom_logger.info("Info message")
custom_logger.warning("Warning message")
custom_logger.error("Error message")
custom_logger.critical("Critical message")

# ------------------------------------------------
# 8. Python Date & Time Module
# ------------------------------------------------

# ------------------------------------------------
# 9. How to use Date & DateTime class
# ------------------------------------------------
current_date = datetime.date.today()
print("Current Date:", current_date)  # Output: YYYY-MM-DD

current_time = datetime.datetime.now()
print("Current DateTime:", current_time)  # Output: YYYY-MM-DD HH:MM:SS

# ------------------------------------------------
# 10. How to use Time Delta Object
# ------------------------------------------------
delta = datetime.timedelta(days=5)
future_date = current_date + delta
print("Date after 5 days:", future_date)  # Output: YYYY-MM-DD

# ------------------------------------------------
# 11. Formatting Date and Time
# ------------------------------------------------
formatted_date = current_time.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date:", formatted_date)  # Output: DD-MM-YYYY HH:MM:SS

# Parsing String to Date
date_string = "01-03-2025"
parsed_date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
print("Parsed Date:", parsed_date)  # Output: 2025-03-01 00:00:00

# ------------------------------------------------
# 12. Python Calendar Module
# ------------------------------------------------
# Display a full calendar for a year
year = 2025
print(calendar.calendar(year))

# ------------------------------------------------
# 13. Text Calendar (Printing Month)
# ------------------------------------------------
month_calendar = calendar.month(2025, 3)
print(month_calendar)

# ------------------------------------------------
# 14. HTML Calendar (Generating an HTML Calendar)
# ------------------------------------------------
html_calendar = calendar.HTMLCalendar().formatmonth(2025, 3)
print(html_calendar)  # Outputs an HTML table

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **Logging Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Log File Configuration**: Writing logs to files, adding timestamps
- **Custom Logger**: Multiple handlers, different formats
- **Exception Logging**: Capture and log exceptions
- **Date-Time Module**: Working with date, time, timedelta
- **Calendar Module**: Displaying text and HTML calendars
"""
