from commands.base_command import BaseCommand

from strategies.gpa_sort_strategy import GPASortStrategy
from strategies.name_sort_strategy import NameSortStrategy
from strategies.age_sort_strategy import AgeSortStrategy
from strategies.id_sort_strategy import IDSortStrategy

class AdvancedSortCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        print("\n========== Advanced Sorting ==========")
        print("1. Sort by GPA")
        print("2. Sort by Name")
        print("3. Sort by Age")
        print("4. Sort by Student ID")

        choice = input("Choose sorting method: ")
        strategies = {
            "1": GPASortStrategy(),
            "2": NameSortStrategy(),
            "3": AgeSortStrategy(),
            "4": IDSortStrategy()
        }
        strategy = strategies.get(choice)

        if not strategy:
            print("Invalid sorting choice.")
            return

        direction = input(
            "\n1. Ascending\n"
            "2. Descending\n"
            "Choose direction: "
        )

        if direction == "1":
            reverse = False

        elif direction == "2":
            reverse = True

        else:
            print("Invalid direction.")
            return

        students = strategy.sort(
            self.manager.students,
            reverse=reverse
        )

        if students:
            for student in students:
                student.display_info()
                print("-" * 30)
        else:
            print("No students found.")