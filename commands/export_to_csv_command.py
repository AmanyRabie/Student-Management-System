from commands.base_command import BaseCommand
from exporters.csv_exporter import CSVExporter


class ExportToCSVCommand(BaseCommand):

    def __init__(self, manager):
        self.manager = manager
        self.exporter = CSVExporter()

    def execute(self):

        students = self.manager.get_all_students()

        if not students:
            print("No students found.")
            return

        self.exporter.export(students)

        print("Students exported successfully to students.csv.")