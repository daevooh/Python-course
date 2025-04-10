# Debugging in Python

This guide covers the basics of debugging Python code, with examples from our driver remittance system project.

## Understanding Errors

Python errors can be categorized into three main types:

1. **Syntax Errors**
   - Occur when Python can't understand your code
   - Usually due to typos or incorrect syntax
   - Example: Missing colon, incorrect indentation

2. **Runtime Errors**
   - Occur while the program is running
   - Example: Division by zero, accessing non-existent list items
   - Also known as exceptions

3. **Logical Errors**
   - Program runs but produces incorrect results
   - Hardest to find and fix
   - Example: Incorrect calculation in payment processing

## Debugging Techniques

### 1. Using Print Statements

The simplest way to debug is by adding print statements:

```python
def calculate_daily_earnings(trips, rate):
    print(f"Debug: trips = {trips}, rate = {rate}")  # Debug print
    earnings = trips * rate
    print(f"Debug: earnings = {earnings}")  # Debug print
    return earnings
```

### 2. Reading Error Messages

Python provides detailed error messages. For example:

```python
# Example of a common error in our project
def process_payment(amount):
    if amount < 0:
        raise ValueError("Payment amount cannot be negative")
    return amount * 1.1  # Adding 10% fee
```

When this function receives a negative amount, it will raise a ValueError with a clear message.

### 3. Using Try-Except Blocks

Handle potential errors gracefully:

```python
def validate_driver_data(name, vehicle_number, rate):
    try:
        if not name:
            raise ValueError("Driver name cannot be empty")
        if not vehicle_number:
            raise ValueError("Vehicle number cannot be empty")
        rate = float(rate)
        if rate <= 0:
            raise ValueError("Rate must be positive")
        return True
    except ValueError as e:
        print(f"Validation error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
```

## Using Stack Overflow Effectively

### 1. How to Search for Solutions
- Use specific error messages in your search
- Include relevant keywords (e.g., "Python", "pandas", "driver remittance")
- Look for recent answers (within 2-3 years)
- Check answer ratings and comments

### 2. How to Ask Questions
- Provide a minimal reproducible example
- Include error messages and tracebacks
- Describe what you've tried
- Share relevant code snippets
- Explain your expected outcome

Example Stack Overflow question format:
```python
# Problem: Calculating driver remittance with negative values
def calculate_remittance(amount, percentage):
    return amount * (percentage / 100)

# Error: Returns negative values when amount is negative
# Expected: Should raise error for negative amounts
# Tried: Adding if amount < 0: return 0, but need proper error handling
```

### 3. Evaluating Answers
- Check if the solution matches your Python version
- Verify if the answer addresses your specific use case
- Consider performance implications
- Look for alternative solutions in comments

## Using Pseudo-Algorithms for Debugging

### 1. What is a Pseudo-Algorithm?
A step-by-step description of how to solve a problem, written in plain language.

### 2. Creating Debugging Pseudo-Algorithms

Example for driver payment validation:
```
PSEUDO-ALGORITHM: Validate Driver Payment
1. START
2. INPUT: payment_amount, driver_id
3. IF payment_amount is not a number THEN
      RAISE TypeError
4. IF payment_amount < 0 THEN
      RAISE ValueError
5. IF driver_id not in database THEN
      RAISE KeyError
6. RETURN True
7. END
```

### 3. Converting Pseudo-Algorithm to Code
```python
def validate_payment(payment_amount, driver_id):
    # Step 3: Check if payment_amount is a number
    if not isinstance(payment_amount, (int, float)):
        raise TypeError("Payment amount must be a number")
    
    # Step 4: Check for negative values
    if payment_amount < 0:
        raise ValueError("Payment amount cannot be negative")
    
    # Step 5: Check driver existence
    if driver_id not in driver_database:
        raise KeyError("Driver not found in database")
    
    return True
```

### 4. Debugging with Pseudo-Algorithms
1. Write the pseudo-algorithm first
2. Identify potential error points
3. Add validation steps
4. Convert to code incrementally
5. Test each step

Example for trip processing:
```
PSEUDO-ALGORITHM: Process Trip
1. START
2. INPUT: trip_data dictionary
3. VALIDATE required fields exist
4. CONVERT data types if needed
5. CALCULATE earnings
6. VALIDATE result is positive
7. RETURN earnings
8. END
```

## Common Errors in Our Project

### 1. Data Type Errors

```python
# Incorrect
daily_earnings = "500"  # String instead of number
total = daily_earnings * 5  # Error: can't multiply string by integer

# Correct
daily_earnings = float("500")  # Convert to number
total = daily_earnings * 5
```

### 2. Division by Zero

```python
# Incorrect
def calculate_average(earnings, days):
    return earnings / days  # Error if days is 0

# Correct
def calculate_average(earnings, days):
    if days == 0:
        return 0
    return earnings / days
```

### 3. Missing Required Data

```python
# Incorrect
def process_trip(trip_data):
    earnings = trip_data['amount'] * trip_data['rate']  # Error if keys don't exist

# Correct
def process_trip(trip_data):
    if 'amount' not in trip_data or 'rate' not in trip_data:
        raise ValueError("Missing required trip data")
    return trip_data['amount'] * trip_data['rate']
```

## Debugging Tools

1. **Python's Built-in Debugger (pdb)**
   ```python
   import pdb
   
   def calculate_weekly_total(daily_earnings):
       pdb.set_trace()  # Set breakpoint
       total = sum(daily_earnings)
       return total
   ```

2. **VS Code Debugger**
   - Set breakpoints
   - Step through code
   - Inspect variables
   - Watch expressions

3. **Print Debugging**
   - Add strategic print statements
   - Use f-strings for detailed output
   - Remove or comment out when done

## Best Practices

1. **Write Defensive Code**
   - Validate inputs
   - Handle edge cases
   - Use type hints
   - Add docstrings

2. **Keep It Simple**
   - Break complex functions into smaller ones
   - Use meaningful variable names
   - Add comments for complex logic

3. **Test Incrementally**
   - Test each function separately
   - Use small, testable inputs
   - Verify output at each step

## Project-Specific Debugging

When working on our driver remittance system, watch out for:

1. **Payment Calculations**
   - Verify all amounts are positive
   - Check percentage calculations
   - Validate date formats

2. **Data Validation**
   - Ensure all required fields are present
   - Validate data types
   - Check for reasonable ranges

3. **File Operations**
   - Verify file paths
   - Check file permissions
   - Handle missing files

## Next Steps

After mastering debugging basics, you'll be ready to:
1. Write more complex functions
2. Handle file operations
3. Work with external data
4. Build the complete remittance system

Remember: Debugging is a skill that improves with practice. Don't get discouraged by errors - they're opportunities to learn!
