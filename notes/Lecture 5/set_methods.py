
# # Set methods 

# set = {1,1,2,3 ,34,5543,4}

# #1 : Add method ---> add the new element in the set 

# print(set,set.add("yash"),type(set))    

# # 2 : Remove method ----> removes the element from the set

# print(set,set.remove(1))

# # 3 : clear method ---> clears the set and returns the empty set 

# print(set,set.clear())


## Important methods 

set1 = {1,34,2,12,12,44}
set2 = {1,32,3,12,69}

# 1. Union Method ---> will take the values from the both sets and returns an set with all unique values from the both set 

print(set1.union(set2))


# 2. Intersection Method ---> it will take the common values from the both set and will return the set with containing that values 

print(set1.intersection(set2))

# -------------------------------------------------------------------------------------------------------------

# ==========================================================
# PYTHON SET — COMPLETE MASTER NOTES (ALL-IN-ONE)
# ==========================================================

# A set is an unordered, mutable collection of UNIQUE elements.
# - No duplicate values allowed
# - Unordered (no indexing, no slicing)
# - Mutable (can add/remove elements)
# - Uses curly braces { }

# ----------------------------------------------------------
# 1. CREATING SET
# ----------------------------------------------------------

s1 = {1, 2, 3, 4}
s2 = {"Yash", 17, True}

empty_set = set()   # Correct way
# wrong = {}        # This creates a dictionary, NOT a set

print(type(s1))  # <class 'set'>

# Duplicate values automatically removed
s3 = {1, 2, 2, 3, 3}
print(s3)  # {1, 2, 3}


# ----------------------------------------------------------
# 2. ADDING ELEMENTS
# ----------------------------------------------------------

s = {1, 2, 3}

s.add(4)              # Add single element
s.update([5, 6])      # Add multiple elements

print(s)


# ----------------------------------------------------------
# 3. REMOVING ELEMENTS
# ----------------------------------------------------------

s.remove(2)   # Remove element (error if not present)
s.discard(10) # Remove safely (no error)
s.pop()       # Remove random element
# s.clear()   # Remove all elements

print(s)


# ----------------------------------------------------------
# 4. SET OPERATIONS (VERY IMPORTANT)
# ----------------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))          # {1,2,3,4,5}
print(a.intersection(b))   # {3}
print(a.difference(b))     # {1,2}
print(a.symmetric_difference(b))  # {1,2,4,5}


# Operators form:
print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference
print(a ^ b)   # Symmetric difference


# ----------------------------------------------------------
# 5. SUBSET & SUPERSET
# ----------------------------------------------------------

x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))
print(y.issuperset(x))


# ----------------------------------------------------------
# 6. MEMBERSHIP
# ----------------------------------------------------------

print(1 in a)
print(10 not in a)


# ----------------------------------------------------------
# 7. COPYING SET
# ----------------------------------------------------------

c = a.copy()
print(c)


# ----------------------------------------------------------
# 8. FROZENSET (IMMUTABLE SET)
# ----------------------------------------------------------

fs = frozenset([1, 2, 3])
print(fs)

# fs.add(4)  # ERROR (immutable)


# ==========================================================
# IMPORTANT THINGS TO REMEMBER
# ==========================================================

# 1. Sets store UNIQUE elements only.
# 2. No indexing, no slicing.
# 3. Order is not guaranteed.
# 4. {} creates dictionary, not empty set.
# 5. remove() gives error if element not present.
# 6. discard() is safer than remove().
# 7. Set operations are very powerful.
# 8. Lookup in set is very fast (O(1) average).
# 9. Use set when uniqueness matters.
# 10. Use frozenset when you need immutable set.


# ==========================================================
# DAILY LIFE USE CASES
# ==========================================================

# - Removing duplicates from list
# - Finding common elements between two datasets
# - Checking unique users in system
# - Comparing tags
# - Filtering duplicate API results
# - Fast membership checking
# - Data science preprocessing


# Example: Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = list(set(numbers))
print(unique_numbers)


# ==========================================================
# COMMON INTERVIEW QUESTIONS
# ==========================================================

# 1. Difference between set and list?
# 2. Why are sets faster for membership testing?
# 3. Difference between remove() and discard()?
# 4. What is symmetric difference?
# 5. Can set contain list as element? Why not?
# 6. What is frozenset?
# 7. How to remove duplicates from list?
# 8. Time complexity of set lookup?
# 9. How to find common elements between two lists?
# 10. Why set elements must be immutable?


# ==========================================================
# REALITY CHECK
# ==========================================================

# If you cannot:
# - Remove duplicates confidently
# - Explain union vs intersection clearly
# - Explain why set cannot contain list
# - Explain why set is faster than list for search
# - Use set to compare two datasets

# Then you don't truly understand sets yet.