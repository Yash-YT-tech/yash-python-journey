num_1 = int(input(("Enter number 1 :")))
num_2 = int(input(("Enter number 2 :")))

multiplication = num_1 * num_2
division = num_1 / num_2
addition = num_1 + num_2
subtraction =  num_1 - num_2
remainder = num_1 % num_2
floor_division = num_1 // num_2

print (multiplication ,division , addition, subtraction,remainder,floor_division)


# ======================================
# PYTHON INPUT FUNCTION — COMPLETE NOTES
# ======================================

# input() is used to take user input from keyboard.
# IMPORTANT: input() ALWAYS returns data as STRING.


# --------------------------------------------------
# 1. BASIC INPUT
# --------------------------------------------------

name = input("Enter your name: ")
print("Hello", name)

# Even if you enter number, it will be stored as string.


# --------------------------------------------------
# 2. INPUT WITH TYPE CASTING
# --------------------------------------------------

# Taking integer input
age = int(input("Enter your age: "))
print("Your age is:", age)

# Taking float input
price = float(input("Enter price: "))
print("Price is:", price)

# If user enters wrong value (like text instead of number),
# program will crash with ValueError.


# --------------------------------------------------
# 3. MULTIPLE INPUTS IN ONE LINE
# --------------------------------------------------

# Taking two integers in one line
a, b = map(int, input("Enter two numbers: ").split())

print("Sum:", a + b)

# How it works:
# input() -> takes string
# split() -> separates by space
# map(int, ...) -> converts each to integer


# --------------------------------------------------
# 4. SPLIT METHOD
# --------------------------------------------------

data = input("Enter values separated by space: ")
values = data.split()

print(values)  # returns list of strings


# --------------------------------------------------
# 5. TAKING LIST INPUT
# --------------------------------------------------

numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# --------------------------------------------------
# 6. IMPORTANT POINTS
# --------------------------------------------------

# input() always returns string
# Use int(), float() if numeric input is needed
# Wrong datatype input -> ValueError
# split() separates input by space
# map() applies function to each element


# --------------------------------------------------
# 7. COMMON BEGINNER MISTAKE
# --------------------------------------------------

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)  # This will CONCATENATE (join strings)

# If you enter 5 and 6
# Output will be 56
# Not 11

# Correct way:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)