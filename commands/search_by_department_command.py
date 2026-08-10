from commands.base_command import BaseCommand

class SearchByDepartmentCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        department = input("Enter department :")
        result = self.manager.search_by_department(department)
        if result:
            for r in result:
                r.display_info()
                print("-" * 30)
        else:
            print("Department not found")
