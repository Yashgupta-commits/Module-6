# Module-6
Task-1
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

Task-2
 Line 1: Create a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A list called numbers is created.
It contains integers from 1 to 10.
This is the original list used for further operations.

 Line 2: Extract First Five Elements
first_five_elements = numbers[0:5]
This line uses list slicing to extract part of the list.
numbers[0:5] means:

 Start from index 0 (which is 1)
 Go up to but not including index 5 (which is 6)
So, first_five_elements = [1, 2, 3, 4, 5]
 These are the first five elements of the original list.

Line 3: Reverse the Extracted List

reversed_list = list(reversed(first_five_elements))

    reversed(first_five_elements) creates an iterator that goes through the list in reverse.

    list(...) converts this iterator back into a regular list.

    Result: reversed_list = [5, 4, 3, 2, 1]

    This gives a new list that is the reverse of the first five elements.

 Line 4: Print the Original List

print("original list", numbers)

    Prints the entire original list:

    original list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Line 5: Print the Extracted First Five Elements

print("Extracted First five elements:", first_five_elements)

    Prints the sliced sublist from the original list:

    Extracted First five elements: [1, 2, 3, 4, 5]

 Line 6: Print the Reversed List

print("Reversed Extracted list:", reversed_list)

    Prints the reversed version of the extracted sublist:

    Reversed Extracted list: [5, 4, 3, 2, 1]

Final Output of the Program

original list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted First five elements: [1, 2, 3, 4, 5]
Reversed Extracted list: [5, 4, 3, 2, 1]


