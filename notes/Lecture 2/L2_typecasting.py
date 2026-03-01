# ======================================
# PYTHON TYPE CASTING — COMPLETE NOTES
# ======================================

# Type casting means converting one data type into another.


# --------------------------------------------------
# 1. IMPLICIT TYPE CASTING (Automatic)
# --------------------------------------------------
# Python automatically converts smaller datatype to larger datatype
# to avoid data loss.

a = 5        # int
b = 2.5      # float

c = a + b    # int automatically converted to float
print(c)     # 7.5
print(type(c))  # float


# --------------------------------------------------
# 2. EXPLICIT TYPE CASTING (Manual)
# --------------------------------------------------
# We manually convert datatype using built-in functions.

# ---- int() ----
x = "10"
y = int(x)     # string -> integer
print(y)
print(type(y))

# ---- float() ----
a = "5.5"
b = float(a)   # string -> float
print(b)
print(type(b))

# ---- str() ----
num = 100
text = str(num)   # integer -> string
print(text)
print(type(text))

# ---- bool() ----
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("Hi"))   # True


# --------------------------------------------------
# 3. LIST, TUPLE, SET CONVERSION
# --------------------------------------------------

l = [1, 2, 3]

t = tuple(l)   # list -> tuple
print(t)

s = set(l)     # list -> set
print(s)

l2 = list(t)   # tuple -> list
print(l2)


# --------------------------------------------------
# 4. IMPORTANT RULES
# --------------------------------------------------

# 1. You can convert numeric strings to numbers:
#    int("10") works
#    int("10.5") does NOT work (use float first)

# 2. You cannot convert letters into numbers:
#    int("abc") -> ValueError

# 3. Float to int removes decimal part (does NOT round)
print(int(5.9))   # 5


# --------------------------------------------------
# 5. COMMON ERRORS
# --------------------------------------------------

# int("10.5") -> Error
# int("hello") -> Error
# float("abc") -> Error


# --------------------------------------------------
# 6. QUICK SUMMARY
# --------------------------------------------------

# int()    -> convert to integer
# float()  -> convert to float
# str()    -> convert to string
# bool()   -> convert to boolean
# list()   -> convert to list
# tuple()  -> convert to tuple
# set()    -> convert to set

# Python allows implicit conversion in arithmetic.
# Manual conversion is called explicit casting.