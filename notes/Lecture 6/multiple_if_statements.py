# if can be independent statement 
# elif and else cannot be a independent statements (they can dependent on the if statements)
# there is no limit for the elif statements 

age = int(input("Enter your age : "))

# if statement No:1

if (age%2==0):
    print("The age is even")

# END if statement No:1 (So , the statement 1 is an independent statement )

# if statement No:2 

if (age>=18):
    print("Welcome to party")

elif (age<0):
    print("You entered negative age , invalid ")

else: 
    print("Not eligible for the party")

#END if statement No:2 (So this , is the if elif else ladder )

print("End of the program \n and Have you noticed the the both \n if statemnts \n had excuted independly without depending on other \n Thank you for your time \n Focus on study whats \n Enjoy party afterwards")




