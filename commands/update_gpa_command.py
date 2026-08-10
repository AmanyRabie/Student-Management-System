from commands.base_command import BaseCommand

class UpdateGPACommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        student_id = int(input("Enter Student ID: "))
        new_gpa = float(input("Enter New GPA: "))
        self.manager.update_gpa(student_id, new_gpa)
        print("GPA updated successfully.")