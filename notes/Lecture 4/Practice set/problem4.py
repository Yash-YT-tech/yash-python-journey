# Problem 4 : Write a programm to sum a list with 4 numbers  

num_list = []
sum_list = []

num_first = int(input("Enter first number : "))
num_list.append(num_first)

num_second = int(input("Enter second number : "))
num_list.append(num_second)

num_third = int(input("Enter third number : "))
num_list.append(num_third)

num_fourth = int(input("Enter fourth number : "))
num_list.append(num_fourth)

sum_num_list = sum(num_list)
sum_list.append(sum_num_list)

print(num_list)
print(sum_list)