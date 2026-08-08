from student import Student
from student_manager import StudentManager

manager = StudentManager()

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
    print("9. Sorted by GPA: ")
    print("10. Student Statistics :")
    print("11. Export Students to CSV")

    choice = input("Enter your choice: ")
    try:

        if choice == "1":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            gpa = float(input("Enter GPA: "))
            student = Student(student_id, name, age, department, gpa)
            manager.add_student(student)
            print("Student added successfully.")
        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            manager.remove_student(student_id)
            print("Student removed successfully.")
        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            student = manager.find_student(student_id)
            if student:
                student.display_info()
            else:
                print("Student not found.")
        elif choice == "4":
            student_id = int(input("Enter Student ID: "))
            new_gpa = float(input("Enter New GPA: "))

            manager.update_gpa(student_id, new_gpa)
            print("GPA updated successfully.")
        elif choice == "5":
            manager.display_all_students()
        elif choice == "6":
            print("Thank you for using the system.")
            break
        elif choice == "7":
            name = input("Enter student name: ")
            result = manager.search_by_name(name)
            if result:
                for r in result:
                    r.display_info()
                    print("-" * 30)
            else:
                print("Student not found")
        elif choice == "8":
            department = input("Enter department :")
            result = manager.search_by_department(department)
            if result:
                for r in result:
                    r.display_info()
                    print("-" * 30)
            else:
                print("Department not found")
        elif choice == "9":
            result = manager.sort_by_gpa()
            if result:
                for r in result:
                    r.display_info()
                    print("-" * 30)
            else:
                print("no students found ")
        elif choice == "10":
            stats = manager.statistics()
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
        elif choice == "11":
            manager.export_to_csv()
            print("Students exported successfully to students.csv.")
 

        
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")
