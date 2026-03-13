# Problem 7 : Write a program to find out whether a given post is talking about “Yash” or not.

print("\n" + "="*50)
print("           Name in Post analysis  ")
print("="*50)
print("\n")

post = input("Enter your Post : ").lower()

if ("yash" in post):
    print("\n"*3)
    print("Result : yes bro they are talking about yash")

else:
    print("\n"*3)
    print("Result : No they are not talking about Yash bro ")