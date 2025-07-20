import os
import bcrypt
from pymongo import MongoClient

# ==========================================
# 🔹 OS Module: Interacting with File System
# ==========================================
print("\n📌 OS Module Usage:")
print(f"Current OS: {os.name}")  # Windows (nt) / Linux (posix)
print(f"Current Directory: {os.getcwd()}")  # Get working directory

# Create a directory
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("✅ Folder 'test_folder' Created")

# Rename folder
if os.path.exists("test_folder"):
    os.rename("test_folder", "renamed_folder")
    print("✅ Folder Renamed to 'renamed_folder'")

# Remove folder
if os.path.exists("renamed_folder"):
    os.rmdir("renamed_folder")
    print("✅ Folder 'renamed_folder' Removed")

# ==========================================
# 🔹 MongoDB Connection (You Can Test This)
# ==========================================
print("\n📌 Connecting to MongoDB...")
client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["users"]
print("✅ MongoDB Connected!")

# ==========================================
# 🔹 MySQL Connection (Concepts Only, Commented)
# ==========================================
# import mysql.connector
# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="your_username",
#         password="your_password",
#         database="your_database"
#     )
#     print("✅ MySQL Connection Successful")
#     cursor = conn.cursor()
# except Exception as e:
#     print(f"❌ MySQL Error: {e}")

# ==========================================
# 🔹 SQL Database (PostgreSQL / Oracle) (Commented Example)
# ==========================================
# import psycopg2
# try:
#     conn = psycopg2.connect(
#         dbname="your_db",
#         user="your_user",
#         password="your_password",
#         host="localhost",
#         port="5432"
#     )
#     print("✅ PostgreSQL Connection Successful")
# except Exception as e:
#     print(f"❌ PostgreSQL Error: {e}")

# ==========================================
# 🔹 MongoDB CRUD Operations
# ==========================================
# Insert single document
user1 = {"name": "Alice", "age": 25, "city": "New York"}
collection.insert_one(user1)
print("✅ Inserted One Document")

# Insert multiple documents
users = [
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 28, "city": "Chicago"}
]
collection.insert_many(users)
print("✅ Inserted Multiple Documents")

# Fetch all documents
print("\n📌 Fetching all users:")
for user in collection.find():
    print(user)

# Fetch one document
print("\n📌 Fetching a single user:")
print(collection.find_one({"name": "Alice"}))

# Update a document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
print("✅ Updated Alice's Age")

# Delete a document
collection.delete_one({"name": "Charlie"})
print("✅ Deleted One Document")

# ==========================================
# 🔹 MongoDB Transactions
# ==========================================
with client.start_session() as session:
    with session.start_transaction():
        collection.insert_one({"name": "David", "balance": 500}, session=session)
        collection.update_one({"name": "David"}, {"$inc": {"balance": -200}}, session=session)
        print("✅ Transaction Successful")

# ==========================================
# 🔹 User Management System (Register & Login)
# ==========================================
def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users = db["users"]
    users.insert_one({"username": username, "password": hashed_password})
    print(f"✅ User '{username}' Registered")

def login_user(username, password):
    users = db["users"]
    user = users.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode(), user["password"]):
        print(f"✅ Login Successful for '{username}'")
    else:
        print(f"❌ Login Failed for '{username}'")

# Run Tests
print("\n📌 User Management System:")
register_user("john_doe", "secure123")
login_user("john_doe", "secure123")  # ✅ Success
login_user("john_doe", "wrongpassword")  # ❌ Fail

# ==========================================
# 🔹 Drop Collection (Cleanup)
# ==========================================
collection.drop()
print("\n✅ All Data Dropped!")
