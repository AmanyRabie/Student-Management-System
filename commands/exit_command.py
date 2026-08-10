from commands.base_command import BaseCommand

class ExitCommand(BaseCommand):

    def execute(self):
        print("Thank you for using the system.")
        return False
