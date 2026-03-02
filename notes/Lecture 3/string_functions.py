# ======================================
# PYTHON STRING FUNCTIONS — COMPLETE NOTES
# ======================================

text = "python programming"


# --------------------------------------------------
# 1. CASE CONVERSION METHODS
# --------------------------------------------------

print(text.upper())        # Converts to uppercase
print(text.lower())        # Converts to lowercase
print(text.capitalize())   # First letter capital
print(text.title())        # First letter of each word capital
print(text.swapcase())     # Upper -> lower and lower -> upper
print(text.casefold())     # Strong lowercase (used for comparisons)


# --------------------------------------------------
# 2. SEARCHING METHODS
# --------------------------------------------------

print(text.find("pro"))      # Returns index (or -1 if not found)
print(text.rfind("p"))       # Finds from right side
print(text.index("pro"))     # Same as find but gives error if not found
print(text.rindex("p"))      # Right index version
print(text.count("p"))       # Count occurrences


# --------------------------------------------------
# 3. CHECKING METHODS (Return True/False)
# --------------------------------------------------

a = "Python123"

print(a.isalnum())   # Letters + numbers
print(a.isalpha())   # Only letters
print(a.isdigit())   # Only digits
print(a.isnumeric()) # Numeric characters
print(a.islower())   # All lowercase?
print(a.isupper())   # All uppercase?
print(a.istitle())   # Title format?
print(a.isspace())   # Only spaces?
print(a.startswith("Py"))
print(a.endswith("23"))


# --------------------------------------------------
# 4. REPLACE & MODIFY METHODS
# --------------------------------------------------

print(text.replace("python", "java"))  # Replace word
print(text.strip())    # Remove spaces both sides
print(text.lstrip())   # Remove left spaces
print(text.rstrip())   # Remove right spaces


# --------------------------------------------------
# 5. SPLIT & JOIN METHODS
# --------------------------------------------------

sentence = "Python is powerful"

words = sentence.split()   # Split by space
print(words)

csv = "a,b,c,d"
print(csv.split(","))      # Split by comma

print("-".join(words))     # Join list into string


# --------------------------------------------------
# 6. ALIGNMENT METHODS
# --------------------------------------------------

word = "Hi"

print(word.center(10))     # Center align
print(word.ljust(10))      # Left align
print(word.rjust(10))      # Right align
print(word.zfill(5))       # Pad with zeros


# --------------------------------------------------
# 7. STRING ENCODING
# --------------------------------------------------

print(text.encode())   # Convert string to bytes


# --------------------------------------------------
# 8. PARTITION METHODS
# --------------------------------------------------

data = "key=value"

print(data.partition("="))   # Splits into 3 parts
print(data.rpartition("="))


# --------------------------------------------------
# 9. EXPAND TABS
# --------------------------------------------------

line = "Hello\tWorld"
print(line.expandtabs(4))


# --------------------------------------------------
# IMPORTANT NOTES
# --------------------------------------------------

# Strings are IMMUTABLE.
# All string methods return NEW string.
# Original string does NOT change unless reassigned.

# Example:
s = "hello"
s.upper()
print(s)        # still "hello"

s = s.upper()
print(s)        # now "HELLO"


# --------------------------------------------------
# MOST IMPORTANT METHODS (Remember These Properly)
# --------------------------------------------------

# upper()
# lower()
# capitalize()
# title()
# find()
# replace()
# split()
# join()
# strip()
# startswith()
# endswith()
# count()