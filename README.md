# Module-6
task-1
1. User Input
 Name = input("Enter the student's name: ")
This line prompts the user to enter a student's name.
 The name entered by the user (e.g., "Charlie") is stored in the variable Name.
The value of Name is a string.

2. Student Marks Dictionary
Student_marks = {"alice": 85, "bob": 50, "Charlie": 92, "David": 7}
    A Python dictionary named Student_marks is created.
It stores student names as keys and their marks as values.
For example:
 "alice" → 85
 "Charlie" → 92

3. Check if Student Exists
if Name in Student_marks:
This line checks if the user's input Name matches exactly any key in the dictionary.
Python is case-sensitive, so:
"charlie" is not the same as "Charlie"
"bob" is different from "Bob"

4. If Student Found
    print(Name + "'s marks:", Student_marks[Name])
If the name exists in the dictionary:
 The program prints the student’s name along with their marks.
 Student_marks[Name] retrieves the mark associated with that name.
For example, if the user entered "Charlie", the output would be:
Charlie's marks: 92

5. If Student Not Found
Student not found






