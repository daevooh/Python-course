# 1. Automating Driver Remittance Checks
# Check if a driver has met their daily target.
remittance = 5000
target = 7000

# a. Check if the target is met
if remittance >= target:
    # b. Print a congratulatory message
    print("Congratulations! You have met your daily target.")
else:
    # c. Calculate and print how much more is needed
    shortfall = target - remittance
    print(f"You need {shortfall} more to meet your daily target.")

# 2. Bonus Eligibility
# Check if a driver qualifies for a bonus.
remittance_threshold = 5000
trip_count_threshold = 20
driver_remittance = 6000
driver_trip_count = 18

# a. Check bonus eligibility
if driver_remittance > remittance_threshold and driver_trip_count >= trip_count_threshold:
    print("Congratulations! You qualify for a bonus.")
else:
    # b. Provide feedback on criteria not met
    if driver_remittance <= remittance_threshold:
        print("You need to increase your remittance to qualify for a bonus.")
    if driver_trip_count < trip_count_threshold:
        print("You need to log more trips to qualify for a bonus.")

# 3. Categorizing Driver Performance
# Classify drivers into categories based on their remittance.
driver_remittance = 700
target_remittance = 1000

if driver_remittance >= target_remittance:
    category = "Met Target"
elif driver_remittance >= target_remittance / 2:
    category = "Halfway There"
else:
    category = "Needs Improvement"
print(f"Driver Performance: {category}")

# 4. Validating Trip Entries
# Check if a trip entry is valid.
trip_distance = 10  # Example value
remittance_amount = 0  # Example value

if trip_distance > 0 and remittance_amount > 0:
    print("Trip entry is valid.")
else:
    print("Error: Trip entry is invalid. Both distance and remittance must be logged.")

# 5. Checking Multiple Conditions
# Check if a driver qualifies for a reward.
meets_target = True
logs_enough_trips = True
has_no_complaints = False

if meets_target and logs_enough_trips and has_no_complaints:
    print("Congratulations! You qualify for a reward.")
else:
    print("You do not qualify for a reward. Please check the criteria.")