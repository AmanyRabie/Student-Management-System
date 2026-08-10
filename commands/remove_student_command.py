from commands.base_command import BaseCommand

class RemoveStudentCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        student_id = int(input("Enter Student ID: "))
        self.manager.remove_student(student_id)
        print("Student removed successfully.")