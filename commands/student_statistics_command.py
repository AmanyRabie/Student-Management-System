from commands.base_command import BaseCommand

class StudentStatisticsCommand(BaseCommand):
    def __init__(self, manager):
        self.manager = manager 

    def execute(self):
        stats = self.manager.statistics()
        if stats:
            print("\n========== Student Statistics ==========")
            print(f"Total Students: {stats['total students = ']}")

            print("\nHighest GPA Student:")
            stats["highest student : "].display_info()

            print("\nLowest GPA Student:")
            stats["lowest student : "].display_info()

            print(f"\nAverage GPA: {stats['average students = ']}") 
       
        else:
            print("No students found.")