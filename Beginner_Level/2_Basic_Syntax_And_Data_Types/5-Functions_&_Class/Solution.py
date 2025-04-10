# Solutions for Functions and Classes Exercises

## 1. Function to Calculate Total Remittance

def calculate_total_remittance(remittances):
    """
    Calculate the total remittance from a list of remittances.
    """
    return sum(remittances)

# Example usage
weekly_remittances = [100, 200, 150, 300, 250, 400, 350]
total = calculate_total_remittance(weekly_remittances)
print("Total Remittance for the Week:", total)

## 2. Function with Default and Keyword Arguments

def greet_driver(name, age=30, location="Unknown"):
    """
    Print a greeting message for the driver with optional age and location.
    """
    print(f"Hello, {name}! You are {age} years old and located in {location}.")

# Example usage
greet_driver("Alice", location="New York")

## 3. Class to Represent a Driver

class Driver:
    def __init__(self, name, id, location):
        """
        Initialize a new Driver object with name, id, and location.
        """
        self.name = name
        self.id = id
        self.location = location

    def log_trip(self, distance, remittance):
        """
        Log a trip with distance and remittance.
        """
        print(f"Trip logged for {self.name}: {distance} km, {remittance} remittance")

# Example usage
driver1 = Driver("John Doe", "ID123", "Lagos")
driver1.log_trip(120, 300)

## 4. Method to Update Driver Location

class Driver:
    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self.location = location

    def log_trip(self, distance, remittance):
        print(f"Trip logged for {self.name}: {distance} km, {remittance} remittance")

    def update_location(self, new_location):
        """
        Update the driver's location.
        """
        self.location = new_location
        print(f"{self.name}'s location updated to {self.location}")

# Example usage
driver1.update_location("Abuja")

## 5. Class to Track Multiple Drivers

class Fleet:
    def __init__(self):
        self.drivers = {}

    def add_driver(self, driver):
        """
        Add a new driver to the fleet.
        """
        self.drivers[driver.id] = driver
        print(f"Driver {driver.name} added to the fleet.")

    def log_trip_for_driver(self, driver_id, distance, remittance):
        """
        Log a trip for a specific driver.
        """
        if driver_id in self.drivers:
            self.drivers[driver_id].log_trip(distance, remittance)
        else:
            print("Driver not found.")

# Example usage
fleet = Fleet()
fleet.add_driver(driver1)
fleet.log_trip_for_driver("ID123", 150, 400)

## 6. Function to Analyze Driver Performance

def analyze_performance(remittances, target):
    """
    Analyze if the driver met their target and is eligible for a bonus.
    """
    total_remittance = sum(remittances)
    met_target = total_remittance >= target
    bonus_eligible = total_remittance > 2000
    return met_target, bonus_eligible

# Example usage
performance = analyze_performance(weekly_remittances, 1500)
print("Met Target:", performance[0])
print("Bonus Eligible:", performance[1])

# These solutions demonstrate the use of functions and classes to solve real-world problems related to driver management and performance analysis. 