# Problem 4 : What will be the length of following set s:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

len_s = len(s)
print(len_s) # output : 2 

## Note : in python if the both the values are same , then python doesnt care about the datatypes whethere its is floating datatype ot the integer datatype 