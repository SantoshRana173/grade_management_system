# student_management_system/management_system.py

import json
from typing import Dict, List
from student import Student

class StudentManagementSystem:
    def __init__(self):
        """Initialize the student management system with an empty dictionary of students."""
        self.students = {}

    def add_student(self, name: str, grades: Dict[str, int]) -> bool:
        """Add a new student to the system."""
        if name not in self.students:
            self.students[name] = Student(name, grades)
            return True
        return False


    def update_grade(self, name: str, subject: str, grade: int) -> bool:
        """Update a specific student's grade for a given subject."""
        if name in self.students:
          self.students[name][subject] = grade
          return True
        return False

    def delete_student(self, name: str) -> bool:
        """Delete a student from the system."""
        if name in self.students:
            del self.students[name]
            return True
        return False

    def display_records(self) -> None:
        """Display all student records with their grades and average grades."""
        return self.students, self.get_average_grade()

    def save_to_file(self, filename: str = "students.json") -> bool:
        """Save all students to a JSON file."""
        try:
            with open(filename, "w") as file:
                json.dump([student.to_dict() for student in self.students.values()], file)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def load_from_file(self, filename: str = "students.json") -> bool:
        """Load student data from a JSON file."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for student_data in data:
                    student = Student.from_dict(student_data)
                    self.students[student.name] = student
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
