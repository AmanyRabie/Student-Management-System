from student import Student
from commands.base_command import BaseCommand

class AddStudentCommand(BaseCommand):
    def __init__(self, manager): # depandency injection
        self.manager = manager

    def execute(self):
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        gpa = float(input("Enter GPA: "))
        student = Student(
            student_id,
            name,
            age, 
            department, 
            gpa
        )
        self.manager.add_student(student)
        print("Student added successfully.")