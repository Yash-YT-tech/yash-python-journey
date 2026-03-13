# problem 4 : Write a program to find whether a given username contains more than 10 characters or not.

username = input("Enter your username : ")

if len(username)>10 :
    print("Username is too long" , print(len(username)))
else:
    print("Username is valid and less than 10 characters")

# for practice write a script to tell the user that how many characters he want to reduce from the given username 