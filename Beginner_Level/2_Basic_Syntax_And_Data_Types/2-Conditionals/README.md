**Understanding Conditionals in Python**
Conditionals are used to make decisions in your code. They allow your program to execute certain actions based on whether a condition is true or false. This is essential for automating tasks and analyzing data, as you'll often need to check if certain criteria are met.


**Key Concepts**

**1. `if` Statement**
The `if` statement is used to execute a block of code if a condition is true.
    # Example
    remittance = 5000
    target = 7000

    if remittance >= target:
        print("Target met!")

**2. `if-else` Statement**
The `if-else` statement allows you to execute one block of code if the condition is true and another block if the condition is false.
    # Example
    remittance = 5000
    target = 7000

    if remittance >= target:
        print("Target met!")
    else:
        print("Target not met. Keep working!")

**3. `if-elif-else` Statement**
The `if-elif-else` statement is used when you have multiple conditions to check.
    # Example
    remittance = 5000
    target = 7000

    if remittance >= target:
        print("Target met!")
    elif remittance >= target * 0.5:
        print("Halfway there!")
    else:
        print("Far from target. Push harder!")

**4. Nested Conditionals**
You can nest conditionals inside other conditionals to check multiple levels of criteria.
    # Example
    remittance = 5000
    target = 7000
    bonus_threshold = 10000

    if remittance >= target:
        if remittance >= bonus_threshold:
            print("Target met with bonus!")
        else:
            print("Target met!")
    else:
        print("Target not met.")

**5. Logical Operators**
Logical operators (`and`, `or`, `not`) are used to combine multiple conditions Allowing you to make more complex decisions in your code. 

1. and Operator
- The and operator returns True if both conditions are true. If either condition is false, it returns False.
- This is useful when you need to check that multiple criteria are met simultaneously.
    remittance = 5000
    target = 7000
    trips_logged = 10

    if remittance >= target and trips_logged >= 10:
        print("Target met with sufficient trips!")
    else:
        print("Either target or trips are insufficient.")

2. or Operator
- The `or` operator returns `True` if **at least one condition** is true. It only returns `False` if **both conditions** are false.
- This is useful when you need to check if **any one of multiple criteria** is met.
    remittance = 5000
    target = 7000
    trips_logged = 10

    if remittance >= target or trips_logged >= 10:
        print("Driver meets at least one criterion!")
    else:
        print("Driver does not meet any criteria.")

3. not Operator
- The `not` operator reverses the result of a condition. If the condition is `True`, `not` makes it `False`, and vice versa.
- This is useful when you need to check if a condition is **not true**.
    remittance = 5000
    target = 7000

    if not(remittance >= target):
        print("Driver has not met the target.")
    else:
        print("Driver has met the target.")