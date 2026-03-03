# \n --> New line
# \t --> Gives space like TAB button
# \" \" --> prints the double quote as it is 
# sentence = "my name is \"Yash\" "

# print(sentence)

# ---------------------------------------------------------# ======================================
# PYTHON ESCAPE SEQUENCE CHARACTERS
# ======================================

# Escape sequences are special characters used inside strings.
# They start with a backslash (\).

# --------------------------------------------------
# 1. NEW LINE (\n)
# --------------------------------------------------

print("Hello\nWorld")
# Output:
# Hello
# World


# --------------------------------------------------
# 2. TAB SPACE (\t)
# --------------------------------------------------

print("Hello\tWorld")
# Adds horizontal tab space


# --------------------------------------------------
# 3. BACKSLASH (\\)
# --------------------------------------------------

print("This is a backslash: \\")
# Output: This is a backslash: \


# --------------------------------------------------
# 4. SINGLE QUOTE (\')
# --------------------------------------------------

print('It\'s Python')
# Used to insert single quote inside single-quoted string


# --------------------------------------------------
# 5. DOUBLE QUOTE (\")
# --------------------------------------------------

print("He said \"Hello\"")
# Used to insert double quote inside double-quoted string


# --------------------------------------------------
# 6. CARRIAGE RETURN (\r)
# --------------------------------------------------

print("Hello\rWorld")
# Moves cursor to beginning of line


# --------------------------------------------------
# 7. BACKSPACE (\b)
# --------------------------------------------------

print("Helloo\b")
# Removes one character before it


# --------------------------------------------------
# 8. FORM FEED (\f)
# --------------------------------------------------

print("Hello\fWorld")
# Rarely used


# --------------------------------------------------
# 9. VERTICAL TAB (\v)
# --------------------------------------------------

print("Hello\vWorld")
# Rarely used


# --------------------------------------------------
# 10. RAW STRING (r" ")
# --------------------------------------------------

# Raw string ignores escape sequences
print(r"Hello\nWorld")
# Output: Hello\nWorld


# --------------------------------------------------
# IMPORTANT NOTES
# --------------------------------------------------

# \n -> new line
# \t -> tab
# \\ -> backslash
# \' -> single quote
# \" -> double quote
# \r -> carriage return
# \b -> backspace

# Escape sequences are mostly used in formatting output and file paths.