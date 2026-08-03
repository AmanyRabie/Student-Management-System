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
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")
