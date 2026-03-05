# Dictionary 
# -key value Pairs 
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

info_yash = {
    "Name" : "Yash",
    "Class": 12,
    "Division" : "King",
    "Smartness" : 100

} # here the name is Key and the yash is the value 
# Key : can use strings, integers 
# Value : can use strings , integers , lists , tuples (All the data types )

print(info_yash,type(info_yash))

print(info_yash["Name"]) # it will only print the value of when we provide it with key 
## Note : if we provide it with value it will return error

##Empty Dictionary 

empty_dictionary={}
print(type(empty_dictionary))