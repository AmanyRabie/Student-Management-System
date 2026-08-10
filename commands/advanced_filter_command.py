from commands.base_command import BaseCommand

class AdvancedFilterCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        name = input("Enter name (or press Enter to skip): ")
        department = input("Enter department (or press Enter to skip): ")

        min_gpa_input = input("Enter minimum GPA (or press Enter to skip): ")
        max_gpa_input = input("Enter maximum GPA (or press Enter to skip): ")

        min_age_input = input("Enter minimum age (or press Enter to skip): ")
        max_age_input = input("Enter maximum age (or press Enter to skip): ")

        name = name if name else None
        department = department if department else None

        min_gpa = float(min_gpa_input) if min_gpa_input else None
        max_gpa = float(max_gpa_input) if max_gpa_input else None

        min_age = int(min_age_input) if min_age_input else None
        max_age = int(max_age_input) if max_age_input else None

        result = self.manager.advanced_filter(
            name=name,
            department=department,
            min_gpa=min_gpa,
            max_gpa=max_gpa,
            min_age=min_age,
            max_age=max_age
        )

        if result:
            for student in result:
                student.display_info()
                print("-" * 30)
        else:
            print("No students match the given filters.")

