# Problem 2 : Write a program to accept marks of 6 students and display them in a sorted manner 

marks = []

student_one_marks = int(input("Marks of Student 1 : "))
marks.append(student_one_marks)

student_two_marks = int(input("Marks of Student 2 : "))
marks.append(student_two_marks)

student_three_marks = int(input("Marks of Student 3 : "))
marks.append(student_three_marks)

student_four_marks = int(input("Marks of Student 4 : "))
marks.append(student_four_marks)

student_five_marks = int(input("Marks of Student 5 : "))
marks.append(student_five_marks)

student_six_marks = int(input("Marks of Student 6 : "))
marks.append(student_six_marks)

sorted_marks = marks.sort()

print(marks)