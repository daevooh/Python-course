# 1. Numbers
# Calculate the total cost of items bought at a market.
yam_price = 500
rice_price = 2500
beans_price = 1500

# a. Calculate the total cost
total_cost = yam_price + rice_price + beans_price

# b. Print the result
print("Total Cost:", total_cost)

# c. Print the data types
print("Data type of yam_price:", type(yam_price))
print("Data type of rice_price:", type(rice_price))
print("Data type of beans_price:", type(beans_price))

# d. Modified print statement to include: string and the variable
print(f"The total cost of items is: {total_cost}")

# 2. Strings
# Create a welcome message for a Nigerian restaurant.
restaurant_name = "Mama Nkechi's Kitchen"
slogan = "Taste the love in every bite!"

# a. Concatenate them and print the result
welcome_message = restaurant_name + " - " + slogan
print("Welcome Message:", welcome_message)

# b. Create a menu and print it as well
menu = "Menu: Jollof Rice, Egusi Soup, Pounded Yam"
print("Restaurant Menu:", menu)

# 3. Convert String to Integer
# Convert a string representation of a phone number to an integer for validation.
phone_number_str = "08012345678"

# a. Create print statement before and after the conversion
print("Phone number (string):", phone_number_str)
phone_number_int = int(phone_number_str)
print("Phone number (integer):", phone_number_int)

# 4. Convert Float to Integer
# Round down the price of an item to the nearest whole number.
price_float = 99.99

# a. Create print statement before and after the conversion
print("Price (float):", price_float)
price_int = int(price_float)
print("Price (integer):", price_int)

# 5. Convert Boolean to String
# Display a message based on whether a student passed an exam.
passed_exam = True

# a. Create print statement before and after the conversion
print("Passed Exam (boolean):", passed_exam)
passed_exam_str = str(passed_exam)
print("Passed Exam (string):", passed_exam_str)
print(f"Student passed the exam: {passed_exam_str}")