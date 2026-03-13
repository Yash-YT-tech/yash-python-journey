# Problem 6 : Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50
# => F



print("\n" + "="*50)
print("           Student marks System  ")
print("="*50)
## -------------------Input Name ---------------------
your_name = input("\nEnter your name please : ").capitalize()


## -------------------------Input Subject 1 -----------------------
print("\n ----------Subject 1-----------")

subject1_name = input("Enter you name of the subject1 : ").capitalize()

marks_subject1 = int(input("Enter your marks for the subject 1 : "))


## -----------------------Input Subject 2----------------------------
print("\n ----------Subject 2 -------------")

subject2_name = input("Enter you name of the subject2 : ").capitalize()

marks_subject2 = int(input("Enter your marks for the subject 2 : "))

##------------------------Total percentage ---------------------------
print("\n --------Total marks percentage -------------")
total_marks_percentage = 100 * (marks_subject1 + marks_subject2) / 200
print(total_marks_percentage)


##-------------------------------Grade allocation-----------------------------

Grade = ""

if (total_marks_percentage > 90 and total_marks_percentage<100):
    Grade = "Excellent"

elif (90 > total_marks_percentage > 80 ):
    Grade = "A"
    

elif ( 80 > total_marks_percentage > 70 ):
    Grade = "B"
    

elif ( 70 > total_marks_percentage > 60):
    Grade = "C"
    

elif (60 >total_marks_percentage > 50):
    Grade = "D"
    

else :
    Grade = "F"
    
##-----------------------------------Final Result-------------------------------------------

print(f"""
------------------------student report ------------------------------------------
      
 Name : {your_name }

 subject 1 : {subject1_name}   
 Marks : {marks_subject1}

 subject 2 : {subject2_name}   
 Marks : {marks_subject2}

 Percentage : {total_marks_percentage}

 Grade : {Grade}

""")


