from commands.base_command import BaseCommand

class SearchByNameCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        name = input("Enter student name: ")
        result = self.manager.search_by_name(name)
        if result:
            for r in result:
                r.display_info()
                print("-" * 30)
        else:
            print("Student not found")
