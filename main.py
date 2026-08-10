from student_manager import StudentManager
from commands.add_student_command import AddStudentCommand
from commands.remove_student_command import RemoveStudentCommand
from commands.find_student_command import FindStudentCommand
from commands.update_gpa_command import UpdateGPACommand
from commands.display_all_student_command import DisplayAllStudentCommand
from commands.exit_command import ExitCommand
from commands.search_by_name_command import SearchByNameCommand
from commands.search_by_department_command import SearchByDepartmentCommand
from commands.student_statistics_command import StudentStatisticsCommand
from commands.export_to_csv_command import ExportToCSVCommand
from commands.advanced_filter_command import AdvancedFilterCommand
from commands.advanced_sort_command import AdvancedSortCommand

manager = StudentManager()
add_student_command = AddStudentCommand(manager)
remove_student_command = RemoveStudentCommand(manager)
find_student_command = FindStudentCommand(manager)
update_gpa_command = UpdateGPACommand(manager)
display_all_student_command = DisplayAllStudentCommand(manager)
exit_command = ExitCommand()
search_by_name_command = SearchByNameCommand(manager)
search_by_department_command = SearchByDepartmentCommand(manager)
statistics_command = StudentStatisticsCommand(manager)
export_csv_command = ExportToCSVCommand(manager)
advanced_filter_command = AdvancedFilterCommand(manager)
advanced_sort_command = AdvancedSortCommand(manager)

commands = {
    "1": add_student_command,
    "2": remove_student_command,
    "3": find_student_command,
    "4": update_gpa_command,
    "5": display_all_student_command,
    "6": exit_command,
    "7": search_by_name_command,
    "8": search_by_department_command,
    "9": statistics_command,
    "10": export_csv_command,
    "11": advanced_filter_command,
    "12": advanced_sort_command 
} 


while True:

    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Find Student")
    print("4. Update GPA")
    print("5. Display All Students")
    print("6. Exit")
    print("7. Search by Name")
    print("8. Search by Department")
    print("9. Student Statistics :")
    print("10. Export Students to CSV")
    print("11. Advanced Filtering :")
    print("12. Advanced Sorting :")

    choice = input("Enter your choice: ")
    try:

        command = commands.get(choice)

        if command:
            result = command.execute()    #polymorphism

            if result is False:
                break
        else:
            print("Invalid choice.")

    except ValueError as e:
        print(f"Error: {e}")

