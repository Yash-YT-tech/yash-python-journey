# Problem 5 : Write a program which finds out whether a given name is present in a list or not.

name_list = ["Yash" , "Ram" , "Shoorveer" , "Deepak" , "Gangaster"]

find_name = input("Enter the name you want to find in the list bro :  ").capitalize()


if (find_name  in name_list):
    print("yes bro the name is present in the list")

else : 
    print("Sorry bro but the the name you have given is not present in our database , wait we will add your name in the list")
    # name_list.append(find_name)

print(name_list)

#doubt 

# hey why the problem is not working as i wanted as when the user enters the new name i want it to store in the list for the next time i want to make my list as the memory or the database so it will take the new username and keep it bro , but my logic is not working here 

## i got the reason bro why this happens and why the databases are important for the same reason bro , because when we run the program it creates a new instance of the list and when we append the new name to the list it is only stored in that instance of the list and when we run the program again it creates a new instance of the list and the new name is not present in that instance of the list so it is not stored in the list for the next time bro , so to solve this problem we need to use databases bro , so that we can store the data permanently and can access it whenever we want bro . 


