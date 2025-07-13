Name = input("Enter the student's name: ")

Student_marks = {"alice": 85,"bob": 50,"Charlie": 92,"David": 7}
if  Name in Student_marks:
    print(Name+"'s marks:",Student_marks[Name])

else:
    print("Student not found")
