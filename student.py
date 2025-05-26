# student_management_system/student.py

from typing import Dict

class Student:
    def __init__(self, name: str, grades: Dict[str, int]):
        """
        Initialize a student with a name and their grades.

        Parameters:
            name (str): Name of the student.
            grades (dict): A dictionary of subjects and grades.
        """
        self.name = name
        self.grades = {}

    def add_grade(self, subject: str, grade: int) -> None:
        """Add or update a grade for a specific subject."""
        self.name[subject] = grade


    def get_average_grade(self) -> float:
        """Calculate the average grade for the student."""
        average = sum(self.grades.values()) / len(self.grades)
        return average

    def to_dict(self) -> Dict[str, any]:
        """Convert the Student instance to a dictionary for JSON serialization."""
        return {
            "name": self.name,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data: Dict[str, any]) -> "Student":
        """Create a Student instance from a dictionary."""
        return Student(data["name"], data["grades"])
