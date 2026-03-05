info_yash = {
    "Name" : "Yash",
    "Class": 12,
    "Division" : "Beta",
    "Dicipline_score" : 100

}

# Dictionary methods (items , keys/values , update , get )

# print(info_yash.items()) # Returns the list of (key value pairs) / all items from the dictionary

# print(info_yash.keys()) # Returns keys in list format

# print(info_yash.values()) # Returns values in list format

info_yash.update({"Division" : "Alpha"}) # as dictionary are mutuable we can upadate the values of the particular key that we wanted 
# we can new key : Value pair in the dict 
info_yash.update({"Who" : "Student"}) # had added the new key and value pair in an existing dict 
print(info_yash) 

## Difference between       
# normal_method = info_yash["Name2"] 
# get_method = info_yash.get["Name2"]

# the the normal_method will return error and the get_method will return none 
# thats the difference between two of them 

info_yash.pop()

# ------------------------------------------------------------------------------------------------------------------

# ==========================================================
# PYTHON DICTIONARY — COMPLETE MASTER NOTES (ALL-IN-ONE)
# ==========================================================

# A dictionary is an unordered (in older Python), 
# insertion-ordered (Python 3.7+) collection of key-value pairs.
# - Mutable
# - Keys must be UNIQUE
# - Keys must be IMMUTABLE (int, str, tuple etc.)
# - Values can be anything


# ----------------------------------------------------------
# 1. CREATING DICTIONARY
# ----------------------------------------------------------

student = {
    "name": "Yash",
    "age": 17,
    "marks": 85
}

empty_dict = {}

print(type(student))  # <class 'dict'>


# ----------------------------------------------------------
# 2. ACCESSING VALUES
# ----------------------------------------------------------

print(student["name"])        # Direct access
print(student.get("age"))     # Safe access (returns None if not found)

# student["grade"]  # ERROR
print(student.get("grade"))   # None (no error)


# ----------------------------------------------------------
# 3. ADDING / UPDATING VALUES
# ----------------------------------------------------------

student["grade"] = "A"      # Add new key
student["age"] = 18         # Update existing key

print(student)


# ----------------------------------------------------------
# 4. REMOVING ITEMS
# ----------------------------------------------------------

student.pop("marks")     # Remove by key
student.popitem()        # Remove last inserted item
# del student["age"]     # Delete specific key
# student.clear()        # Remove all items

print(student)


# ----------------------------------------------------------
# 5. DICTIONARY METHODS
# ----------------------------------------------------------

data = {"a": 1, "b": 2, "c": 3}

print(data.keys())        # All keys
print(data.values())      # All values
print(data.items())       # Key-value pairs (tuple form)

data.update({"d": 4})     # Add multiple values
print(data)

copy_data = data.copy()   # Copy dictionary
print(copy_data)


# ----------------------------------------------------------
# 6. LOOPING THROUGH DICTIONARY
# ----------------------------------------------------------

for key in data:
    print(key)

for value in data.values():
    print(value)

for key, value in data.items():
    print(key, value)


# ----------------------------------------------------------
# 7. CHECKING MEMBERSHIP
# ----------------------------------------------------------

print("a" in data)        # Checks key only
print(1 in data.values()) # Check value manually


# ----------------------------------------------------------
# 8. NESTED DICTIONARY
# ----------------------------------------------------------

students = {
    "student1": {"name": "Yash", "age": 17},
    "student2": {"name": "Rahul", "age": 18}
}

print(students["student1"]["name"])


# ----------------------------------------------------------
# 9. DICTIONARY COMPREHENSION (VERY IMPORTANT)
# ----------------------------------------------------------

squares = {x: x*x for x in range(5)}
print(squares)


# ----------------------------------------------------------
# 10. FROMKEYS METHOD
# ----------------------------------------------------------

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)


# ==========================================================
# IMPORTANT THINGS TO REMEMBER
# ==========================================================

# 1. Dictionary stores data as key:value pairs.
# 2. Keys must be UNIQUE.
# 3. Keys must be IMMUTABLE.
# 4. Dictionary is MUTABLE.
# 5. get() is safer than direct indexing.
# 6. keys(), values(), items() are heavily used.
# 7. update() adds or modifies values.
# 8. pop() removes by key.
# 9. Looping using items() is best practice.
# 10. Dictionary comprehension is powerful.


# ==========================================================
# DAILY LIFE USE CASES
# ==========================================================

# - Storing user data (name, email, password)
# - API responses (JSON format)
# - Database records
# - Configuration settings
# - Counting word frequency
# - Mapping product ID to price
# - Storing model predictions in AI
# - Login authentication systems


# ==========================================================
# COMMON INTERVIEW QUESTIONS
# ==========================================================

# 1. Difference between dictionary and list?
# 2. Why must dictionary keys be immutable?
# 3. Difference between get() and []?
# 4. What is dictionary comprehension?
# 5. How to merge two dictionaries?
# 6. What happens if duplicate keys are used?
# 7. How to iterate over dictionary?
# 8. How to remove a key?
# 9. What is time complexity of dictionary lookup?
# 10. Why dictionary is faster than list for searching?


# ==========================================================
# REALITY CHECK
# ==========================================================

# If you cannot:
# - Count word frequency using dictionary
# - Merge two dictionaries
# - Explain why list cannot be dictionary key
# - Explain difference between get() and []
# - Explain hash table concept (basic idea)

# Then you don’t fully understand dictionary yet.

 