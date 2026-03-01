# ======================================
# PYTHON OPERATORS — COMPLETE NOTES
# ======================================

# Operators are used to perform operations on variables and values.


# --------------------------------------------------
# 1. ARITHMETIC OPERATORS
# --------------------------------------------------

a = 10
b = 3

print(a + b)   # Addition -> 13
print(a - b)   # Subtraction -> 7
print(a * b)   # Multiplication -> 30
print(a / b)   # Division -> 3.333...
print(a % b)   # Modulus (remainder) -> 1
print(a ** b)  # Exponent (power) -> 1000
print(a // b)  # Floor division -> 3


# --------------------------------------------------
# 2. COMPARISON OPERATORS
# --------------------------------------------------

x = 5
y = 10

print(x == y)   # Equal to -> False
print(x != y)   # Not equal -> True
print(x > y)    # Greater than -> False
print(x < y)    # Less than -> True
print(x >= y)   # Greater than or equal
print(x <= y)   # Less than or equal


# --------------------------------------------------
# 3. LOGICAL OPERATORS
# --------------------------------------------------

a = True
b = False

print(a and b)   # True only if both are True
print(a or b)    # True if at least one is True
print(not a)     # Reverse the result


# --------------------------------------------------
# 4. ASSIGNMENT OPERATORS
# --------------------------------------------------

num = 10

num += 5   # num = num + 5
num -= 2   # num = num - 2
num *= 3   # num = num * 3
num /= 2   # num = num / 2
num %= 4   # num = num % 4
num **= 2  # num = num ** 2
num //= 3  # num = num // 3

print(num)


# --------------------------------------------------
# 5. IDENTITY OPERATORS
# --------------------------------------------------

# Used to compare memory location

a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True (same object)
print(a is c)      # False (different object)
print(a is not c)  # True


# --------------------------------------------------
# 6. MEMBERSHIP OPERATORS
# --------------------------------------------------

text = "Python"

print("P" in text)        # True
print("z" not in text)    # True


# --------------------------------------------------
# 7. BITWISE OPERATORS (Advanced)
# --------------------------------------------------

x = 5   # 0101
y = 3   # 0011

print(x & y)   # AND
print(x | y)   # OR
print(x ^ y)   # XOR
print(~x)      # NOT
print(x << 1)  # Left shift
print(x >> 1)  # Right shift


# ======================================
# IMPORTANT POINTS TO REMEMBER
# ======================================

# Arithmetic -> + - * / % ** //
# Comparison -> == != > < >= <=
# Logical -> and or not
# Assignment -> = += -= *= /= ...
# Identity -> is , is not
# Membership -> in , not in
# Bitwise -> &, |, ^, ~, <<, >>

# Operators follow precedence rules like mathematics.
# Brackets () have highest priority.