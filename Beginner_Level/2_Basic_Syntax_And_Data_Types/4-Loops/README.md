 Loops in Python

## Overview
Loops are used to automate repetitive tasks in Python. They allow you to iterate over a sequence of items (like lists, tuples, or dictionaries) or repeat a block of code until a condition is met. Loops are essential for tasks like processing multiple trip entries, calculating totals, and analyzing trends.

---

## **Types of Loops**
 **1. `for` Loop**
The `for` loop is used to iterate over a sequence (like a list, tuple, or dictionary) and perform actions on each item.

**Real-Life Scenario: Processing Trip Entries**
- **Scenario:** A driver logs multiple trip entries for the day. Use a `for` loop to process each trip and calculate the total remittance.

# Example: Processing trip entries
total_remittance = 0
for remittance in trip_remittances:
    total_remittance += remittance
    print("Total Remittance for the Day:", total_remittance)

---

### **2. `while` Loop**
The `while` loop is used to repeat a block of code as long as a condition is true.

### **Real-Life Scenario: Validating Trip Entries**
- **Scenario:** A driver logs trip entries, but you need to ensure that all entries are valid (e.g., remittance is greater than zero). Use a `while` loop to prompt the driver until a valid entry is provided.


# Example: Validating trip entries
remittance = -1
while remittance <= 0:
    remittance = int(input("Enter a valid remittance amount (greater than 0): "))
print("Valid remittance logged:", remittance)


### **3. Nested Loops**
Nested loops are loops inside other loops. They are useful for processing multi-dimensional data.

### **Real-Life Scenario: Logging Multiple Drivers' Trips**
- **Scenario:** You want to log trip entries for multiple drivers. Use nested loops to process each driver's trips.


# Example: Logging multiple drivers' trips
drivers = {
    "Jane": [4000, 6000, 9000],
    "Jane": [4000, 6000, 9000],
    "John": [3000, 5000, 7000]
}

for driver, trips in drivers.items():
    print(f"Driver: {driver}")
    for trip in trips:
        print(f"  Trip Remittance: {trip}")

---

### **4. Loop Control Statements**
Loop control statements (`break`, `continue`, and `pass`) allow you to modify the behavior of loops.

#### **Real-Life Scenario: Stopping at Invalid Entries**
- **Scenario:** A driver logs trip entries, but you want to stop processing if an invalid entry (e.g., negative remittance) is encountered.

# Example: Stopping at invalid entries
trip_remittances = [5000, 7000, -8000, 6000]
for remittance in trip_remittances:
    if remittance < 0:
        print("Invalid entry encountered. Stopping processing.")
        break
    print(f"Processing remittance: {remittance}")