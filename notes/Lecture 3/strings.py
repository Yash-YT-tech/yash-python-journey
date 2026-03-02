# strings are immutable (You cannot chnage in existing string)

# string slicing :

name = "Yash"

name_part = name[0:4] # the End index will be not printed 
 # and the start of the string is from zero (0)

print(name_part)

# Negative slicing 
# if given negative slicing convert it to positive slicing and find out the anwser 

# skip value 
# [1:4:2]
# 1 = Start Value , 4 = so end will be 3 , 2 = skip the valur by jumping by 2 and start from next number but the first number will be included in the answer  


# -------------------------------------------------------------------

# ======================================
# PYTHON STRINGS — COMPLETE NOTES
# ======================================

# A string is a sequence of characters.
# Strings are IMMUTABLE (cannot be changed after creation).

# --------------------------------------------------
# 1. CREATING STRINGS
# --------------------------------------------------

a = "Hello"
b = 'World'
c = """This is
multi-line string"""

print(a)
print(type(a))   # str


# --------------------------------------------------
# 2. STRING INDEXING
# --------------------------------------------------

text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n (negative indexing starts from end)

# Index starts from 0


# --------------------------------------------------
# 3. STRING SLICING
# --------------------------------------------------

word = "Programming"

print(word[0:6])   # Progra
print(word[:6])    # Progra
print(word[3:])    # gramming
print(word[-4:])   # ming

# Format: string[start:end]
# end is excluded


# --------------------------------------------------
# 4. STRING LENGTH
# --------------------------------------------------

name = "Yash"
print(len(name))   # 4


# --------------------------------------------------
# 5. STRING METHODS (IMPORTANT)
# --------------------------------------------------

text = "python programming"

print(text.upper())       # PYTHON PROGRAMMING
print(text.lower())       # python programming
print(text.capitalize())  # Python programming
print(text.title())       # Python Programming

print(text.find("pro"))   # returns index
print(text.replace("python", "Java"))

print(text.count("p"))    # count occurrences

print(text.startswith("py"))  # True
print(text.endswith("ing"))   # True


# --------------------------------------------------
# 6. STRING STRIP FUNCTIONS
# --------------------------------------------------

data = "   hello   "

print(data.strip())   # removes spaces both sides
print(data.lstrip())  # removes left spaces
print(data.rstrip())  # removes right spaces


# --------------------------------------------------
# 7. STRING CONCATENATION
# --------------------------------------------------

first = "Hello"
second = "World"

print(first + " " + second)


# --------------------------------------------------
# 8. STRING REPETITION
# --------------------------------------------------

print("Hi " * 3)


# --------------------------------------------------
# 9. ESCAPE SEQUENCES
# --------------------------------------------------

print("Hello\nWorld")  # new line
print("Hello\tWorld")  # tab space
print("He said \"Hi\"")  # double quote inside string


# --------------------------------------------------
# 10. MEMBERSHIP OPERATORS
# --------------------------------------------------

text = "Python"

print("P" in text)        # True
print("z" not in text)    # True


# --------------------------------------------------
# 11. STRING FORMAT METHODS
# --------------------------------------------------

name = "Yash"
age = 17

# Old method
print("My name is {} and I am {} years old".format(name, age))

# f-string (BEST METHOD)
print(f"My name is {name} and I am {age} years old")


# --------------------------------------------------
# 12. IMPORTANT RULES
# --------------------------------------------------

# Strings are immutable.
# You cannot change a character directly.

# text[0] = "H"  -> ERROR

# To modify string, create new string.


# --------------------------------------------------
# 13. COMMON BEGINNER MISTAKES
# --------------------------------------------------

# 1. Forgetting that slicing excludes end index.
# 2. Trying to modify string directly.
# 3. Forgetting input() gives string.
# 4. Using + with numbers without type conversion.


# --------------------------------------------------
# QUICK SUMMARY
# --------------------------------------------------

# Indexing -> string[index]
# Slicing -> string[start:end]
# Length -> len(string)
# Upper/Lower -> change case
# Replace -> change word
# Find -> get index
# Strip -> remove spaces
# f-string -> best formatting method
# Strings are IMMUTABLE