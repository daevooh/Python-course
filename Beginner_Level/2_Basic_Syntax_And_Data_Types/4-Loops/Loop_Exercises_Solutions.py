# Loop Exercises Solutions

# 1. Calculating Total Remittances
# Calculate the total remittance for the week using a for loop.
weekly_remittances = [100, 200, 150, 300, 250, 400, 350]
total_remittance = 0
for remittance in weekly_remittances:
    total_remittance += remittance
print(f"Total Remittance for the Week: {total_remittance}")

# 2. Validating Trip Entries
# Prompt the driver until a valid remittance is provided using a while loop.
remittance = -1
while remittance <= 0:
    remittance = int(input("Enter a valid remittance amount (greater than 0): "))
print(f"Valid Remittance Logged: {remittance}")

# 3. Processing Multiple Drivers' Trips
# Process each driver's trips using a nested loop and calculate the total remittance.
drivers_trips = {
    "Alice": [100, 200, 150],
    "Bob": [300, 250, 400],
    "Charlie": [350, 400, 450]
}
for driver in drivers_trips:
    total = 0
    for trip in drivers_trips[driver]:
        total += trip
    print(f"Driver: {driver}, Total Remittance: {total}")

# 4. Skipping Invalid Entries
# Iterate over trip entries and skip invalid entries using the continue statement.
trip_remittances = [100, -50, 200, 300, -100, 400]
for remittance in trip_remittances:
    if remittance < 0:
        continue
    print(f"Valid Remittance: {remittance}")

# 5. Stopping at Invalid Entries
# Iterate over trip entries and stop processing if an invalid entry is found using the break statement.
for remittance in trip_remittances:
    if remittance < 0:
        print("Invalid entry encountered. Stopping processing.")
        break
    print(f"Processing Remittance: {remittance}")

# 6. Calculating Average Remittance
# Calculate the total and average daily remittance using a for loop.
total_remittance = 0
for remittance in weekly_remittances:
    total_remittance += remittance
average_remittance = total_remittance / len(weekly_remittances)
print(f"Average Daily Remittance: {average_remittance}")

# 7. Categorizing Drivers Based on Performance
# Categorize drivers based on their remittance performance.
drivers_performance = {
    "Alice": 1200,
    "Bob": 800,
    "Charlie": 600
}
target_remittance = 1000
for driver in drivers_performance:
    remittance = drivers_performance[driver]
    if remittance >= target_remittance:
        category = "Met Target"
    elif remittance >= target_remittance / 2:
        category = "Halfway There"
    else:
        category = "Needs Improvement"
    print(f"Driver: {driver}, Category: {category}")

# Example usage
if __name__ == "__main__":
    # Example data
    weekly_remittances = [100, 200, 150, 300, 250, 400, 350]
    drivers_trips = {
        "Alice": [100, 200, 150],
        "Bob": [300, 250, 400],
        "Charlie": [350, 400, 450]
    }
    trip_remittances = [100, -50, 200, 300, -100, 400]
    drivers_performance = {
        "Alice": 1200,
        "Bob": 800,
        "Charlie": 600
    }
    target_remittance = 1000

    # Run solutions
    calculate_total_remittances(weekly_remittances)
    # validate_trip_entries()  # Uncomment to run interactively
    process_multiple_drivers_trips(drivers_trips)
    skip_invalid_entries(trip_remittances)
    stop_at_invalid_entries(trip_remittances)
    calculate_average_remittance(weekly_remittances)
    categorize_drivers(drivers_performance, target_remittance) 