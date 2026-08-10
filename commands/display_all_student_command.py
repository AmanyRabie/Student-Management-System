from commands.base_command import BaseCommand

class DisplayAllStudentCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    from commands.base_command import BaseCommand


class DisplayAllStudentCommand(BaseCommand):

    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        students = self.manager.get_all_students()

        if not students:
            print("No students found.")
            return

        for student in students:
            student.display_info()
            print("-" * 30)