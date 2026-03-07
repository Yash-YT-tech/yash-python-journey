# The space after we press enter in (if/elif/else) is know as indentation 
# The if elif else , following is known as id elif else ladder 
# This are known as conditional statements 


age = int(input("Enter you age : "))
num = 18 - age

if (age>=18):
    print("You are eligible for the driving License")

elif (age<0):
    print(f"Its an Invalid input , age can't be negative bro and you entered {age}")

elif (age>75):
    print("You are old bro , just chill and enjoy your lifes ramining days")

else: 
    print(f"Sorry you no eligible, please wait {num} more years for your driving license")

print("Thank you for using our program")
print("End of the program")


# ---------------------------------------------------------------------------------------------------------------

# ==========================================================
# PYTHON CONDITIONAL STATEMENTS — COMPLETE MASTER NOTES
# ==========================================================

# Conditional statements allow decision making in programs.
# Syntax uses:
# if
# elif
# else

# ----------------------------------------------------------
# 1. BASIC IF STATEMENT
# ----------------------------------------------------------

age = 18

if age >= 18:
    print("You are eligible to vote")


# ----------------------------------------------------------
# 2. IF-ELSE
# ----------------------------------------------------------

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ----------------------------------------------------------
# 3. IF-ELIF-ELSE
# ----------------------------------------------------------

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ----------------------------------------------------------
# 4. MULTIPLE CONDITIONS (LOGICAL OPERATORS)
# ----------------------------------------------------------

age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")

if age < 18 or not citizen:
    print("Not eligible")


# ----------------------------------------------------------
# 5. NESTED IF
# ----------------------------------------------------------

num = 15

if num > 0:
    if num % 5 == 0:
        print("Positive and divisible by 5")
    else:
        print("Positive but not divisible by 5")
else:
    print("Negative number")


# ----------------------------------------------------------
# 6. SHORT-HAND IF (One-line)
# ----------------------------------------------------------

a = 10
b = 20

if a < b: print("a is smaller")


# ----------------------------------------------------------
# 7. TERNARY OPERATOR (IMPORTANT)
# ----------------------------------------------------------

result = "Even" if a % 2 == 0 else "Odd"
print(result)


# ----------------------------------------------------------
# 8. PASS STATEMENT
# ----------------------------------------------------------

x = 5

if x > 0:
    pass  # placeholder, does nothing


# ----------------------------------------------------------
# 9. MATCH CASE (Python 3.10+) — Advanced
# ----------------------------------------------------------

value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")


# ----------------------------------------------------------
# 10. TRUTHY AND FALSY VALUES
# ----------------------------------------------------------

# False values:
# False, None, 0, "", [], {}, set()

if "":
    print("Won't run")
else:
    print("Empty string is False")


# ----------------------------------------------------------
# IMPORTANT THINGS TO REMEMBER
# ----------------------------------------------------------

# 1. Indentation matters in Python.
# 2. Conditions must return True or False.
# 3. Order of elif matters (top-down execution).
# 4. Use logical operators carefully (and, or, not).
# 5. Nested if reduces readability if overused.
# 6. Always handle edge cases.
# 7. == is comparison, = is assignment.
# 8. Avoid unnecessary nesting.
# 9. Short-circuit evaluation happens in logical operators.
# 10. Use ternary operator for simple conditions only.


# ----------------------------------------------------------
# DAILY LIFE USE CASES
# ----------------------------------------------------------

# - Login authentication
# - Age validation
# - ATM withdrawal rules
# - Discount calculation
# - Traffic light system
# - Input validation
# - Grading system
# - Access control in applications
# - AI decision branches
# - Game logic


# ----------------------------------------------------------
# COMMON INTERVIEW QUESTIONS
# ----------------------------------------------------------

# 1. Difference between if and elif?
# 2. What is short-circuit evaluation?
# 3. What is ternary operator?
# 4. Difference between == and is?
# 5. What are truthy and falsy values?
# 6. How to avoid deep nested if?
# 7. What happens if multiple conditions are True?
# 8. What is the order of execution in if-elif-else?
# 9. Can we use multiple elif?
# 10. When to use match-case instead of if-elif?


# ----------------------------------------------------------
# REALITY CHECK
# ----------------------------------------------------------

# If you cannot:
# - Write prime number checker
# - Validate password rules
# - Check leap year
# - Build simple login system
# - Handle multiple edge cases

# Then your conditional logic is weak.