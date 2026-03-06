# Problem 2 : Write a program to input eight numbers from the user and display all the unique numbers (once).

unique_num = set()

num1 = int(input("Enter your 1st Number :"))
unique_num.add(num1)

num2 = int(input("Enter your 2nd Number :"))
unique_num.add(num2)

num3 = int(input("Enter your 3rd Number :"))
unique_num.add(num3)

num4 = int(input("Enter your 4th Number :"))
unique_num.add(num4)

num5 = int(input("Enter your 5th Number :"))
unique_num.add(num5)

num6 = int(input("Enter your 6th Number :"))
unique_num.add(num6)

num7 = int(input("Enter your 7th Number :"))
unique_num.add(num7)

num8 = int(input("Enter your 8th Number :"))
unique_num.add(num8)


print(unique_num)