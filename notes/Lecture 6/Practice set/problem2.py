# Problem 2 : Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks_info_dict = {}


name = input("Enter your name : ")

subject1 = input("Enter the name of subject 1 :")
capital_sub1 = subject1.capitalize()

subject2 = input("Enter the name of subject 2 :")
capital_sub2 = subject2.capitalize()

subject3 = input("Enter the name of subject 3 :")
capital_sub3 = subject3.capitalize()

marks1 =  float(input("Enter marks of subject 1 :"))
marks2 =  float(input("Enter marks of subject 2 :"))
marks3 =  float(input("Enter marks of subject 3 :"))

marks_info_dict.update({capital_sub1:marks1})
marks_info_dict.update({capital_sub2:marks2}) 
marks_info_dict.update({capital_sub3:marks3})


marks1_percentage = 100*(marks1)/100
marks2_percentage = 100*(marks2)/100
marks3_percentage = 100*(marks3)/100
total_percentage = (100*(marks1+marks2+marks3))/300

# Marks cannot be more than 100 or less than zero (to check the allated marks)

if (marks1>100 or marks1<0 or
    marks2>100 or marks2<0 or
    marks3>100 or marks3<0) : 

     print("Entered marks are invalid ")
     exit()

 

# To check if the student is passed or failed 

if marks1_percentage>=33 and marks2_percentage>=33 and marks3_percentage>=33 and total_percentage>=40:
    print(f"Congrats {name} you are PASSED,celebrate")

else:
    print("Feeling bad for you bro , you are FAILED")
    print(f"{name} this is not the end of the life this is just start you can retry {name}")


print(marks_info_dict)
print(f'''Percentage for chapter 1 :{marks1_percentage} 
Percentage for chapter 2 :{marks2_percentage} 
Percentage for chapter 3 :{marks3_percentage}
Total Percentage : {total_percentage} ,
this are your marks {name}''')



# make a dictionary to store subject and marks of the student

