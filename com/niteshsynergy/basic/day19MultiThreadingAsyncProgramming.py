"""
Python Multi-threading & Async Programming - Complete Guide
"""

import threading
import time
import asyncio
import concurrent.futures

# ------------------------------------------------
# 1. What is Multi-threading?
# ------------------------------------------------
"""
- Multi-threading allows a program to run multiple operations concurrently.
- Uses multiple threads within a single process.
- Ideal for I/O-bound tasks (e.g., downloading files, reading disk data).
"""

# ------------------------------------------------
# 2. What is Async Programming?
# ------------------------------------------------
"""
- Asynchronous programming allows non-blocking execution of tasks.
- It uses `asyncio` for handling concurrent operations.
- Ideal for tasks like database queries, network requests, and I/O operations.
"""

# ------------------------------------------------
# 3. Threading Module in Python
# ------------------------------------------------
def print_numbers():
    for i in range(5):
        print(f"Thread: {i}")
        time.sleep(1)

# Creating a thread
thread = threading.Thread(target=print_numbers)
thread.start()

# Main program runs while thread executes
print("Main thread is running")

# Wait for thread to complete
thread.join()
print("Thread execution completed")

# ------------------------------------------------
# 4. Creating Multiple Threads
# ------------------------------------------------
def print_task(task_id):
    print(f"Task {task_id} is running")
    time.sleep(2)
    print(f"Task {task_id} completed")

# Creating multiple threads
threads = []
for i in range(3):
    thread = threading.Thread(target=print_task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# ------------------------------------------------
# 5. Thread Synchronization using Lock
# ------------------------------------------------
lock = threading.Lock()
counter = 0

def increase_counter():
    global counter
    with lock:
        local_counter = counter
        time.sleep(0.1)  # Simulate processing time
        counter = local_counter + 1
        print(f"Counter: {counter}")

# Creating multiple threads with lock
threads = []
for i in range(5):
    thread = threading.Thread(target=increase_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final Counter:", counter)

# ------------------------------------------------
# 6. Daemon Threads (Background Threads)
# ------------------------------------------------
def background_task():
    while True:
        print("Running background task...")
        time.sleep(2)

# Creating a daemon thread
daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()

# Main thread continues execution
time.sleep(5)  # Let the daemon thread run for a while
print("Main thread exiting...")

# ------------------------------------------------
# 7. Python Async Programming using asyncio
# ------------------------------------------------
async def async_function():
    print("Async task started")
    await asyncio.sleep(2)
    print("Async task completed")

# Running an async function
asyncio.run(async_function())

# ------------------------------------------------
# 8. Using asyncio for Multiple Async Tasks
# ------------------------------------------------
async def async_task(task_id):
    print(f"Task {task_id} started")
    await asyncio.sleep(3)  # Simulating async operation
    print(f"Task {task_id} completed")

async def run_tasks():
    tasks = [async_task(i) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(run_tasks())

# ------------------------------------------------
# 9. Async Function with I/O Operation
# ------------------------------------------------
async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulating network delay
    return "Data received"

async def process_data():
    data = await fetch_data()
    print(f"Processing {data}")

asyncio.run(process_data())

# ------------------------------------------------
# 10. Using ThreadPoolExecutor for Multi-threading
# ------------------------------------------------
def heavy_computation(n):
    time.sleep(2)
    return f"Computed {n**2}"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(heavy_computation, i) for i in range(5)]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

# ------------------------------------------------
# 11. Using ProcessPoolExecutor for Multi-processing
# ------------------------------------------------
import multiprocessing

def compute_square(n):
    time.sleep(1)
    return f"Square of {n}: {n**2}"

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(compute_square, range(5))
    for result in results:
        print(result)

# ------------------------------------------------
# 12. Combining Threading and Asyncio
# ------------------------------------------------
async def async_function():
    print("Async function running...")
    await asyncio.sleep(2)
    print("Async function done")

def start_asyncio():
    asyncio.run(async_function())

thread = threading.Thread(target=start_asyncio)
thread.start()
thread.join()

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **Multi-threading**:
  - Runs multiple tasks concurrently in the same process.
  - Ideal for I/O-bound tasks.
  - Uses `threading` module.
  - Supports synchronization with `Lock`.
  - Supports background execution with Daemon Threads.

- **Async Programming**:
  - Uses `asyncio` for non-blocking execution.
  - Uses `async`, `await` for async functions.
  - Handles network, database, and I/O operations efficiently.

- **ThreadPoolExecutor & ProcessPoolExecutor**:
  - ThreadPoolExecutor: Manages multiple threads efficiently.
  - ProcessPoolExecutor: Used for CPU-bound tasks.

- **Mixing Threading & Asyncio**:
  - Threading can run `asyncio` loops using `threading.Thread`.

- **Real-world applications**:
  - Web scraping
  - Concurrent API requests
  - File I/O operations
  - Background data processing
"""


"""
Python Multi-threading & Multi-processing - Complete Guide
"""

import threading
import time
import multiprocessing

# ------------------------------------------------
# 1. Introduction
# ------------------------------------------------
"""
- Multi-threading and multi-processing are techniques to execute multiple tasks in parallel.
- **Multi-threading**: Uses multiple threads in the same process (I/O-bound tasks).
- **Multi-processing**: Uses multiple processes (CPU-bound tasks).
"""

# ------------------------------------------------
# 2. Multi-tasking vs Multi-threading
# ------------------------------------------------
"""
- **Multi-tasking**: Executing multiple tasks simultaneously.
- **Multi-threading**: A subset of multi-tasking where multiple threads run within a single process.
"""

# ------------------------------------------------
# 3. Threading Module in Python
# ------------------------------------------------
"""
- Python provides the `threading` module for creating threads.
- Threads share the same memory space, making data sharing easy but also introducing race conditions.
"""

# ------------------------------------------------
# 4. Creating a Thread - Using `Thread` Class
# ------------------------------------------------
def print_numbers():
    for i in range(5):
        print(f"Thread: {i}")
        time.sleep(1)  # Simulate processing time

# Creating and starting a thread
thread = threading.Thread(target=print_numbers)
thread.start()

# Main thread execution
print("Main thread is running...")

# Wait for thread to complete
thread.join()
print("Thread execution completed")

# ------------------------------------------------
# 5. Creating a Thread - Using Class Inheritance
# ------------------------------------------------
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"MyThread: {i}")
            time.sleep(1)

# Creating and starting thread
thread_obj = MyThread()
thread_obj.start()
thread_obj.join()

# ------------------------------------------------
# 6. Creating a Thread - Using Callable Object
# ------------------------------------------------
class Task:
    def __call__(self):
        for i in range(3):
            print(f"Task {i}")
            time.sleep(1)

# Creating a thread with callable object
task = Task()
thread_callable = threading.Thread(target=task)
thread_callable.start()
thread_callable.join()

# ------------------------------------------------
# 7. Life Cycle of a Thread
# ------------------------------------------------
"""
1. New - Thread is created but not started.
2. Runnable - Thread is ready to run.
3. Running - Thread is executing.
4. Blocked - Thread is waiting (e.g., sleep(), I/O operation).
5. Terminated - Thread execution is completed.
"""

# ------------------------------------------------
# 8. Single-threaded Application
# ------------------------------------------------
def single_task():
    for i in range(5):
        print(f"Single Thread Task: {i}")
        time.sleep(1)

single_task()  # Runs sequentially

# ------------------------------------------------
# 9. Multi-threaded Application
# ------------------------------------------------
def multi_task(task_id):
    print(f"Task {task_id} is running")
    time.sleep(2)
    print(f"Task {task_id} completed")

threads = []
for i in range(3):
    thread = threading.Thread(target=multi_task, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# ------------------------------------------------
# 10. Can we call run() directly?
# ------------------------------------------------
"""
- Calling `run()` directly executes the function in the main thread.
- `start()` creates a new thread.
"""

class DemoThread(threading.Thread):
    def run(self):
        print("Running in a separate thread")

t = DemoThread()
t.run()  # Runs in the main thread
t.start()  # Runs in a new thread

# ------------------------------------------------
# 11. Need for `start()` Method
# ------------------------------------------------
"""
- `start()` launches the thread and calls `run()` internally.
- Avoid calling `run()` directly to ensure a new thread is created.
"""

# ------------------------------------------------
# 12. Sleep() - Pausing Execution
# ------------------------------------------------
def task_with_delay():
    print("Task started...")
    time.sleep(3)  # Pause for 3 seconds
    print("Task completed!")

thread = threading.Thread(target=task_with_delay)
thread.start()
thread.join()

# ------------------------------------------------
# 13. Join() - Waiting for Thread Completion
# ------------------------------------------------
"""
- `join()` ensures the main program waits for thread completion.
"""

# ------------------------------------------------
# 14. Synchronization - Lock Class
# ------------------------------------------------
lock = threading.Lock()
counter = 0

def increment_counter():
    global counter
    with lock:
        local_counter = counter
        time.sleep(0.1)
        counter = local_counter + 1
        print(f"Counter: {counter}")

threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final Counter:", counter)

# ------------------------------------------------
# 15. Multi-processing in Python
# ------------------------------------------------
"""
- Unlike threads, each process runs independently with separate memory space.
- Python provides the `multiprocessing` module.
"""

def process_task(name):
    print(f"Process {name} is running")
    time.sleep(2)
    print(f"Process {name} completed")

# Creating processes
if __name__ == "__main__":
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# ------------------------------------------------
# 16. Case Study - Multi-threaded Data Processing
# ------------------------------------------------
import requests

URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched data from {url}: {response.status_code}")

threads = []
for url in URLS:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# ------------------------------------------------
# Summary
# ------------------------------------------------
"""
- **Multi-threading**:
  - Allows multiple tasks to run in a single process.
  - Uses the `threading` module.
  - Best for **I/O-bound** tasks.
  - Threads share memory, requiring synchronization using `Lock`.

- **Multi-processing**:
  - Runs tasks in separate processes.
  - Uses the `multiprocessing` module.
  - Best for **CPU-bound** tasks.
  - Processes do not share memory.

- **Key Concepts**:
  - `start()` vs `run()`
  - `join()` - Waits for thread/process completion.
  - `sleep()` - Delays execution.
  - `Lock` - Prevents race conditions in multi-threading.

- **Case Study**:
  - Multi-threaded API requests using `requests` library.
"""
