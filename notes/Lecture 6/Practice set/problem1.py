# Problem 1 : Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter 1st number : "))

num2 = int(input("Enter 2st number : "))

num3 = int(input("Enter 3st number : "))

num4 = int(input("Enter 4st number : "))

if num1>num2 and num1>num3 and num1>num4 :
    print("Greatest number is :",num1)

elif num2>num1 and num2>num3 and num2>num4 :
    print("Greatest number is :",num2)

elif num3>num1 and num3>num2 and num3>num4 :
    print("greatest number is :",num3)

else:
    print("Greatest number is :",num4)

print("Thank you")