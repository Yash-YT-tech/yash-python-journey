list = [1 , "Yash" , True , False , "World is slow" , "Bro you are"]
print(list)

# List methods :- (sort , reverse , append , insert , pop , remove)

list.append("God") # Append --> adds at the last of the list (apply at the end = append)
print(list)

listnum = [1 ,3 , 42323, 323.43 ,2323 , 533]
listnum.sort() # Sort ----> sorts from small to big and only works with int and float values 
print(listnum)

list.reverse() #Reverse --> it only reverses the list the last index will be first and the first index will be the last 
print(list)

list.insert(4,"is here bro ") # Insert --> list.insert(index on which you want to put on , it will just insert the given argumnet on the particular and index and the orignal argumnet on that index will be shifted towards the next index)
print(list)

list.pop(0)
print(list)

list.remove(1) #Remove ---> removes the index which we have given in argument
print(list)

print(listnum.pop(0)) # it will print the pop value which we have poped out of of the list 
print(listnum)



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ==========================================================
# PYTHON LIST — COMPLETE MASTER NOTES (ALL-IN-ONE)
# ==========================================================

# A list is an ordered, mutable collection.
# - Ordered → maintains insertion order
# - Mutable → can be changed
# - Allows duplicates
# - Can store mixed data types


# ----------------------------------------------------------
# 1. CREATING LISTS
# ----------------------------------------------------------

numbers = [1, 2, 3, 4]
mixed = [1, "Yash", 3.14, True]
empty_list = []

print(type(numbers))  # <class 'list'>


# ----------------------------------------------------------
# 2. INDEXING
# ----------------------------------------------------------

nums = [10, 20, 30, 40]

print(nums[0])    # First element
print(nums[-1])   # Last element (negative indexing)


# ----------------------------------------------------------
# 3. SLICING
# ----------------------------------------------------------

print(nums[0:2])   # [10, 20]
print(nums[:3])    # [10, 20, 30]
print(nums[1:])    # [20, 30, 40]


# ----------------------------------------------------------
# 4. MODIFYING LIST (Because it is MUTABLE)
# ----------------------------------------------------------

nums[0] = 100
print(nums)


# ----------------------------------------------------------
# 5. ADDING ELEMENTS
# ----------------------------------------------------------

lst = [1, 2, 3]

lst.append(4)            # Adds single element at end
lst.insert(1, 10)        # Insert at specific index
lst.extend([5, 6])       # Add multiple elements

print(lst)


# ----------------------------------------------------------
# 6. REMOVING ELEMENTS
# ----------------------------------------------------------

lst.remove(10)   # Remove by value (first occurrence)
lst.pop()        # Remove last element
lst.pop(0)       # Remove by index
# lst.clear()    # Remove all elements

print(lst)


# ----------------------------------------------------------
# 7. SEARCHING & COUNTING
# ----------------------------------------------------------

nums = [1, 2, 2, 3, 4]

print(nums.index(2))   # First occurrence index
print(nums.count(2))   # Count occurrences


# ----------------------------------------------------------
# 8. SORTING & REVERSING
# ----------------------------------------------------------

nums = [4, 1, 3, 2]

nums.sort()                 # Sort ascending (modifies original)
nums.sort(reverse=True)     # Sort descending
nums.reverse()              # Reverse order

print(nums)

# sorted() → returns new sorted list
new_sorted = sorted(nums)
print(new_sorted)


# ----------------------------------------------------------
# 9. COPYING LIST
# ----------------------------------------------------------

a = [1, 2, 3]
b = a.copy()     # Correct copy

# b = a  → both refer to same memory (NOT real copy)

print(b)


# ----------------------------------------------------------
# 10. LENGTH
# ----------------------------------------------------------

print(len(a))


# ----------------------------------------------------------
# 11. LIST COMPREHENSION (VERY IMPORTANT)
# ----------------------------------------------------------

squares = [x*x for x in range(5)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)


# ----------------------------------------------------------
# 12. NESTED LIST
# ----------------------------------------------------------

matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])  # Access nested element


# ----------------------------------------------------------
# 13. MEMBERSHIP OPERATORS
# ----------------------------------------------------------

print(3 in [1, 2, 3])
print(5 not in [1, 2, 3])


# ==========================================================
# IMPORTANT THINGS TO REMEMBER
# ==========================================================

# 1. Lists are MUTABLE.
# 2. append() → add one item.
# 3. extend() → add multiple items.
# 4. remove() → remove by value.
# 5. pop() → remove by index.
# 6. sort() modifies original list.
# 7. sorted() returns new list.
# 8. b = a is reference copy (not real copy).
# 9. Use list comprehension for clean code.
# 10. Lists are heavily used in real-world programming.


# ==========================================================
# DAILY LIFE USE CASES
# ==========================================================

# - Storing student marks
# - Shopping cart items
# - API responses
# - Dataset storage in AI/ML
# - File names from directory
# - Gym workout tracking
# - User input storage


# ==========================================================
# COMMON INTERVIEW QUESTIONS
# ==========================================================

# 1. Difference between list and tuple?
# 2. Difference between append() and extend()?
# 3. Difference between remove() and pop()?
# 4. What happens if you do b = a?
# 5. How to remove duplicates from a list?
# 6. How to reverse a list?
# 7. What is list comprehension?
# 8. Difference between sort() and sorted()?
# 9. Time complexity of append()?
# 10. How to flatten a nested list?
