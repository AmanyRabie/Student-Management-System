from commands.base_command import BaseCommand

class FindStudentCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        student_id = int(input("Enter Student ID: "))
        student = self.manager.find_student(student_id)
        if student:
            student.display_info()
        else:
            print("Student not found.")