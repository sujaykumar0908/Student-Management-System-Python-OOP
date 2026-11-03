"""
Student Management System
Beginner-friendly Python OOP project.

OOP concepts demonstrated:
1. Class and Object
2. Constructor (__init__)
3. Encapsulation (private __marks attribute)
4. Inheritance (Student inherits from Person)
5. Polymorphism (display_details is overridden)
"""

class Person:
    """Base class containing common person information."""

    def __init__(self, name):
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")


class Student(Person):
    """Student class inherits from Person."""

    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name)
        self.student_id = student_id
        self.age = age
        self.course = course
        self.__marks = 0
        self.set_marks(marks)

    def set_marks(self, marks):
        """Encapsulation: marks are updated through this method."""
        if 0 <= marks <= 100:
            self.__marks = marks
            return True
        return False

    def get_marks(self):
        return self.__marks

    def display_details(self):
        """Overrides Person.display_details (polymorphism)."""
        print("-" * 35)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.__marks}/100")
        print("-" * 35)


class StudentManagementSystem:
    """Manages student records using Student objects."""

    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Add Student ---")
        student_id = input("Enter student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        if self.find_student(student_id):
            print("A student with this ID already exists.")
            return

        name = input("Enter student name: ").strip()
        course = input("Enter course: ").strip()

        try:
            age = int(input("Enter age: "))
            marks = float(input("Enter marks (0-100): "))
        except ValueError:
            print("Age and marks must be numbers.")
            return

        if age <= 0:
            print("Age must be greater than zero.")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(student_id, name, age, course, marks)
        self.students.append(student)
        print("Student added successfully!")

    def display_students(self):
        print("\n--- Student Records ---")
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display_details()

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student(self):
        print("\n--- Search Student ---")
        student_id = input("Enter student ID to search: ").strip()
        student = self.find_student(student_id)

        if student:
            print("Student found:")
            student.display_details()
        else:
            print("Student not found.")

    def update_marks(self):
        print("\n--- Update Student Marks ---")
        student_id = input("Enter student ID: ").strip()
        student = self.find_student(student_id)

        if not student:
            print("Student not found.")
            return

        try:
            new_marks = float(input("Enter new marks (0-100): "))
        except ValueError:
            print("Marks must be a number.")
            return

        if student.set_marks(new_marks):
            print("Marks updated successfully!")
        else:
            print("Marks must be between 0 and 100.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        student_id = input("Enter student ID to delete: ").strip()
        student = self.find_student(student_id)

        if student:
            self.students.remove(student)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    def run(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Student Marks")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.display_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_marks()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Thank you for using Student Management System!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
