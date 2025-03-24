Python’s versatility and ease of learning make it perfect for beginners. However, understanding the basics of data types, variables, and operators is crucial to mastering Python programming.
Data Types in Python
Data types are an essential concept in any programming language as they determine the type of data that can be stored and manipulated in a program. Python supports various built-in data types such as numbers, strings, lists, tuples, sets, and dictionaries. Understanding these data types is essential for any Python programming endeavor.

Numbers
Numbers are one of the fundamental data types in Python. There are three types of numbers in Python — integers, floating-point numbers, and complex numbers. Integers are whole numbers without any decimal point. Floating-point numbers are numbers with decimal points. Complex numbers are a combination of real and imaginary numbers.

# Example of numbers in Python
num1 = 5     # integer
num2 = 3.14  # floating-point number
num3 = 2 + 3j  # complex number
Strings
Strings are used to represent text data in Python. They are enclosed within single or double quotes. Python provides many built-in functions and methods to manipulate strings.

# Example of strings in Python
str1 = 'Hello, World!'  # single quotes
str2 = "Python is awesome"  # double quotes
Lists
Lists are used to store a collection of items in Python. They are ordered and mutable, which means you can add, remove or modify elements in a list. Lists are created using square brackets.

# Example of lists in Python
list1 = [1, 2, 3, 4, 5]  # integers
list2 = ["apple", "banana", "cherry"]  # strings
Tuples
Tuples are similar to lists, but they are immutable, which means you cannot modify them after they are created. They are created using round brackets.

# Example of tuples in Python
tuple1 = (1, 2, 3, 4, 5)  # integers
tuple2 = ("apple", "banana", "cherry")  # strings
Sets
Sets are used to store a collection of unique items in Python. They are unordered and mutable, which means you can add or remove elements from a set. Sets are created using curly brackets.

# Example of sets in Python
set1 = {1, 2, 3, 4, 5}  # integers
set2 = {"apple", "banana", "cherry"}  # strings
Dictionaries
Dictionaries are used to store key-value pairs in Python. They are unordered and mutable, which means you can add, remove, or modify elements in a dictionary. Dictionaries are created using curly brackets and colons.

# Example of dictionaries in Python
dict1 = {"name": "John", "age": 30, "city": "New York"}  # strings and integers
dict2 = {"apple": 1, "banana": 2, "cherry": 3}  # strings and integers
Variables in Python
Another fundamental concept in programming is variables. In Python, variables are used to store values that can be accessed and manipulated throughout a program.

Declaring Variables
In Python, declaring a variable is as simple as assigning a value to a name. You do not need to specify a data type as Python is a dynamically typed language, meaning that the interpreter infers the data type from the value that is assigned to the variable. For example, to assign the value 5 to a variable named “x”, you can use the following code:

x = 5
The variable “x” now holds the value 5. You can also assign different types of values to the same variable. For example, you can assign a string value to the variable “x” as follows:

x = "Hello, world!"
This assigns the string “Hello, world!” to the variable “x”.

Using Variables
Once you have declared a variable, you can use it throughout your program. You can print the value of a variable using the print() function. For example, to print the value of the variable “x”, you can use the following code:

print(x)
This will output the value of the variable “x”, which is “Hello, world!”.

You can also use variables in expressions. For example, you can add two variables together as follows:

x = 5
y = 10
z = x + y
print(z)
This assigns the value 15 to the variable “z” and prints it to the console.

Variable Names
When naming variables in Python, there are some rules that you should follow.

Variable names must start with a letter or underscore character (_), and can only contain letters, numbers, and underscores.
Variable names are case-sensitive, meaning that “x” and “X” are two different variables.
It is also recommended to use descriptive variable names that reflect the purpose of the variable.
Operators in Python
Operators are special symbols or keywords that are used to perform operations on values or variables. They allow you to manipulate data and perform calculations in your code.

There are several types of operators in Python, including arithmetic operators, comparison operators, logical operators, and assignment operators. Let’s take a closer look at each type of operator and how it works.

Arithmetic Operators
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division, modulus, and exponentiation. Here are some examples:

x = 10
y = 5

# Addition
result = x + y
print(result) # Output: 15

# Subtraction
result = x - y
print(result) # Output: 5

# Multiplication
result = x * y
print(result) # Output: 50

# Division
result = x / y
print(result) # Output: 2.0

# Modulus
result = x % y
print(result) # Output: 0

# Exponentiation
result = x ** y
print(result) # Output: 100000
Comparison Operators:
Comparison operators are used to comparing two values and return a Boolean value (True or False) based on the result of the comparison. Here are some examples:

x = 10
y = 5

# Greater than
result = x > y
print(result) # Output: True

# Less than
result = x < y
print(result) # Output: False

# Equal to
result = x == y
print(result) # Output: False

# Not equal to
result = x != y
print(result) # Output: True

# Greater than or equal to
result = x >= y
print(result) # Output: True

# Less than or equal to
result = x <= y
print(result) # Output: False
Logical Operators
Logical operators are used to combining two or more conditions and return a Boolean value (True or False) based on the result of the combination. Here are some examples:

x = 10
y = 5
z = 8

# AND operator
result = x > y and x < z
print(result) # Output: False

# OR operator
result = x > y or x < z
print(result) # Output: True

# NOT operator
result = not(x > y)
print(result) # Output: False
Assignment Operators
Assignment operators are used to assigning values to variables. Here are some examples:

x = 10

# Simple assignment
y = x
print(y) # Output: 10

# Addition assignment
x += 5
print(x) # Output: 15

# Subtraction assignment
x -= 3
print(x) # Output: 12

# Multiplication assignment
x *= 2
print(x) # Output: 24

# Division assignment
x /= 4
print(x) # Output: 6.0

# Modulus assignment
x %= 2
print(x) # Output: 0

# Exponentiation assignment
x **= 3
print(x) # Output: 0




https://intellipaat.com/blog/wp-content/uploads/2022/10/Python-Cheat-Sheet-2022.pdf 
https://www-dummies-com.webpkgcache.com/doc/-/s/www.dummies.com/category/books/python-33606/