# Problem 4 :- Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# path of directory (change this to your folder path)
directory_path = "/home/yash/Downloads/YashxPython"

# get contents of directory
files = os.listdir(directory_path)

# print each item
for items in files:
    print(items)