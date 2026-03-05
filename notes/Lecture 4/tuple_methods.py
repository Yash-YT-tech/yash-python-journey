#Tuple has methods (as tey are immutable)
# List has the functions (as they are mutable)

# Tuple Methods : ( count , )

tuple = ("yash",1,"GOD",23,"rain",1,2,4,545,343.43)

counting = tuple.count(1)# Count --> Counts that how many times the particular element appers in the tuple 
print(counting) 

index_of_tuple = tuple.index(545)# Index --> give the index of the element that we wanted 
print(index_of_tuple)

## Note : the tuple methods scans the tuple from the left to right and will print wher the conditions statisfy ; example if we uswe the uindex method for finding the element 1 in the tuple which occurs at the index (1 and 5 ) , but wehn we run the print funtion to count the index of the 1 , it will return the index as only 1 and not the 5 as the as the work is already satisfy with the the ndex 1 and the tuple will stop the method and in the outpu we will see the index as only 1 and not 1 and 5 .     

# List operations : 
# > List operations will not chnage the orignal tuple it will just create the new tuple and we can print that new tuple 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ==========================================================
# PYTHON TUPLE — COMPLETE MASTER NOTES (ALL-IN-ONE)
# ==========================================================

# A tuple is an ordered, IMMUTABLE collection.
# - Ordered → maintains insertion order
# - Immutable → cannot be changed after creation
# - Allows duplicates
# - Faster than list (generally)
# - Uses parentheses ( )


# ----------------------------------------------------------
# 1. CREATING TUPLES
# ----------------------------------------------------------

t1 = (1, 2, 3)
t2 = ("Yash", 17, True)
empty_tuple = ()

print(type(t1))  # <class 'tuple'>

# IMPORTANT: Single element tuple needs comma
single = (5,)   # correct
# wrong = (5)   # This is int, not tuple


# ----------------------------------------------------------
# 2. INDEXING
# ----------------------------------------------------------

nums = (10, 20, 30, 40)

print(nums[0])    # 10
print(nums[-1])   # 40


# ----------------------------------------------------------
# 3. SLICING
# ----------------------------------------------------------

print(nums[0:2])   # (10, 20)
print(nums[:3])    # (10, 20, 30)
print(nums[1:])    # (20, 30, 40)


# ----------------------------------------------------------
# 4. IMMUTABILITY (IMPORTANT)
# ----------------------------------------------------------

# nums[0] = 100   # ERROR → tuple does not support item assignment

# You cannot:
# - add elements
# - remove elements
# - modify elements

# But if tuple contains mutable object inside,
# that object CAN change.

t = ([1, 2], 3)
t[0].append(4)
print(t)   # ([1, 2, 4], 3)


# ----------------------------------------------------------
# 5. TUPLE METHODS (ONLY TWO REAL METHODS)
# ----------------------------------------------------------

nums = (1, 2, 2, 3, 4)

print(nums.count(2))   # Count occurrences
print(nums.index(3))   # First occurrence index


# ----------------------------------------------------------
# 6. LENGTH
# ----------------------------------------------------------

print(len(nums))


# ----------------------------------------------------------
# 7. NESTED TUPLES
# ----------------------------------------------------------

nested = ((1, 2), (3, 4))
print(nested[1][0])   # 3


# ----------------------------------------------------------
# 8. TUPLE PACKING & UNPACKING (VERY IMPORTANT)
# ----------------------------------------------------------

# Packing
person = ("Yash", 17, "India")

# Unpacking
name, age, country = person

print(name)
print(age)
print(country)


# ----------------------------------------------------------
# 9. CONVERTING TUPLE <-> LIST
# ----------------------------------------------------------

t = (1, 2, 3)

l = list(t)    # tuple to list
l.append(4)

t = tuple(l)   # list back to tuple
print(t)


# ----------------------------------------------------------
# 10. MEMBERSHIP
# ----------------------------------------------------------

print(3 in (1, 2, 3))
print(5 not in (1, 2, 3))


# ==========================================================
# IMPORTANT THINGS TO REMEMBER
# ==========================================================

# 1. Tuples are IMMUTABLE.
# 2. Only two methods: count() and index().
# 3. Faster than lists for fixed data.
# 4. Use when data should not change.
# 5. Single element tuple must have comma.
# 6. Tuple unpacking is powerful.
# 7. Used as dictionary keys (because immutable).


# ==========================================================
# DAILY LIFE USE CASES
# ==========================================================

# - Storing fixed configuration values
# - Coordinates (x, y)
# - RGB color values
# - Returning multiple values from functions
# - Database records (fixed structure)
# - Latitude and longitude
# - API response pairs


# ==========================================================
# COMMON INTERVIEW QUESTIONS
# ==========================================================

# 1. Difference between list and tuple?
# 2. Why are tuples faster than lists?
# 3. Can tuple contain mutable objects?
# 4. Why can tuple be dictionary key but list cannot?
# 5. What is tuple unpacking?
# 6. How to create single-element tuple?
# 7. When should you use tuple instead of list?
# 8. How to convert tuple to list?
# 9. Is tuple really completely immutable?
# 10. What is packing and unpacking?


# ==========================================================
# REALITY CHECK
# ==========================================================

# If you cannot explain:
# - Why tuple is immutable
# - Why list cannot be dictionary key
# - What happens when tuple contains list inside
# - How unpacking works

# Then you don't properly understand tuples yet.