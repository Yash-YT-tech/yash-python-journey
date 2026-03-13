# Problem 3 : A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

comment = input("Enter your comment : ")

if ("Make a lot of money" in comment or
    "buy now" in comment or
    "subscribe this" in comment or
    "click this" in comment) : 

    print("This is a spam comment , be safe bro !!")

if ("Message from comapany" in comment or 
    "HR message" in comment or
    "URGENT Meetings" in comment):
    print("Bro this seems an important message , please go through it once ")

else :
    print("Don't worry bro enjoy reading message")

