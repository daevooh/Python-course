# 1. Tracking Daily Remittances
# Store the remittance amounts in a list.
daily_remittances = [100, 200, 150, 300, 250, 400, 350]

# Calculate the total remittance for the week.
total_remittance = sum(daily_remittances)
print("Total Remittance for the Week:", total_remittance)

# Find the highest remittance.
highest_remittance = max(daily_remittances)
print("Highest Remittance:", highest_remittance)

# Add a new remittance for an extra day.
daily_remittances.append(500)
print("Updated Remittances:", daily_remittances)

# 2. Storing Driver Details
# Create a tuple to store the driver's details.
driver_details = ("John Doe", "ID123", "Lagos")

# Access and print each detail individually.
print("Driver Name:", driver_details[0])
print("Driver ID:", driver_details[1])
print("Driver Location:", driver_details[2])

# 3. Immutable Driver Records
# Create a tuple to store driver details.
driver_record = ("John Doe", "ID123", "Lagos")

# Attempt to modify one of the details and observe the result.
try:
    driver_record[1] = "ID456"  # This will raise an error
except TypeError as e:
    print("Error:", e)