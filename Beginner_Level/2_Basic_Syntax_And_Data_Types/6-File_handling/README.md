# Understanding File Handling in Python

File handling is an essential part of programming, allowing you to read from and write to files. This is crucial for tasks like data storage, configuration management, and data analysis.

## Basic File Operations

### Opening a File
To open a file in Python, use the `open()` function. You can specify the mode in which to open the file, such as read ('r'), write ('w'), append ('a'), or read and write ('r+').

```python
# Open a file for reading
file = open('example.txt', 'r')

# Open a file for writing
file = open('example.txt', 'w')
```

### Reading from a File
You can read the contents of a file using methods like `read()`, `readline()`, or `readlines()`.

```python
# Read the entire file
content = file.read()

# Read a single line
line = file.readline()

# Read all lines into a list
lines = file.readlines()
```

### Writing to a File
To write data to a file, use the `write()` method. If the file doesn't exist, it will be created.

```python
# Write a string to a file
file.write('Hello, World!')
```

### Closing a File
Always close a file after you're done with it to free up system resources.

```python
file.close()
```

### Using `with` Statement
The `with` statement is used to open a file and ensure it is properly closed after its suite finishes, even if an exception is raised.

```python
with open('example.txt', 'r') as file:
    content = file.read()
```

## Real-Life Scenario: Managing Driver Logs
- **Scenario**: In the final project, you'll need to manage driver logs by reading from and writing to files.
- **Solution**: Use file handling to store trip data, remittances, and driver details in text or CSV files.

### Example: Writing Driver Logs to a File
```python
driver_logs = [
    'Driver: John Doe, Trip: 120 km, Remittance: 300',
    'Driver: Jane Smith, Trip: 150 km, Remittance: 350'
]

with open('driver_logs.txt', 'w') as file:
    for log in driver_logs:
        file.write(log + '\n')
```

### Example: Reading Driver Logs from a File
```python
with open('driver_logs.txt', 'r') as file:
    logs = file.readlines()
    for log in logs:
        print(log.strip())
```

File handling is a powerful tool for managing data in your applications. By understanding these concepts, you'll be able to efficiently handle data storage and retrieval in your final project.
