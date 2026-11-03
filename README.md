# Student Management System (Python OOP)

## Project overview
The Student Management System is a beginner-level, menu-driven Python program. It lets a user add, view, search, update marks, and delete student records.

This project is created to demonstrate Object-Oriented Programming (OOP) concepts in Python.

## OOP concepts used

1. **Class and Object:** `Person`, `Student`, and `StudentManagementSystem` are classes. Objects are created from these classes.
2. **Constructor:** The `__init__()` method initializes objects.
3. **Encapsulation:** The student's marks are stored in the private attribute `__marks`. The `get_marks()` and `set_marks()` methods control access and updates.
4. **Inheritance:** `Student` inherits from the `Person` class.
5. **Polymorphism:** `Student` overrides the `display_details()` method from `Person`.

## Features

- Add a student record
- Display all student records
- Search for a student using student ID
- Update a student's marks
- Delete a student record
- Validate age and marks

## Requirements

- Python 3.8 or later
- No external libraries are required

## How to run

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Sample run

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
Enter your choice (1-6): 1

--- Add Student ---
Enter student ID: S101
Enter student name: Anu
Enter course: BCA
Enter age: 19
Enter marks (0-100): 88
Student added successfully!

===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
Enter your choice (1-6): 2

--- Student Records ---
-----------------------------------
Student ID : S101
Name       : Anu
Age        : 19
Course     : BCA
Marks      : 88.0/100
-----------------------------------

===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit
Enter your choice (1-6): 6
Thank you for using Student Management System!
```

## Important note

Student records are stored in memory while the program is running. They are cleared when the program exits. This keeps the project simple and suitable for beginners.

## Author

Add your name and class details here before submitting.
