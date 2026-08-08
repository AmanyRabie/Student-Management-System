import json
import os
import csv
from student import Student
class StudentManager:
    def __init__(self):
        self.students =[] 
        self.load_students()

    def add_student(self, student):
         # student => object from class student 
        for s in self.students :
            if s.student_id == student.student_id:
                raise ValueError("Student ID already exists.")
        self.students.append(student)
        self.save_students()

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def remove_student(self, student_id):
        student = self.find_student(student_id)
        if student: 
             self.students.remove(student)
             self.save_students()
        else:
             raise ValueError("Student not found.")

    def update_gpa(self, student_id, new_gpa):
        student = self.find_student(student_id)
        if student:
            student.gpa = new_gpa
            self.save_students()
        else:
             raise ValueError("Student not found.")

    def display_all_students(self):
        if not self.students:
            print("no students found ")
            return
        for s in self.students:
            s.display_info()
            print("-" * 30)

    def save_students(self, filename="students.json"):
        filepath = os.path.join(os.path.dirname(__file__), filename)

        with open(filepath, "w", encoding="utf-8") as file:
            data = [student.to_dict() for student in self.students]
            json.dump(data, file, indent=4, ensure_ascii=False)




    def load_students(self, filename="students.json"):
        filepath = os.path.join(os.path.dirname(__file__), filename)

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.students = []

            for item in data:
                student = Student.from_dict(item)
                self.students.append(student)

        except FileNotFoundError:
            self.students = []

    def search_by_name(self, name):
        result =[]
        for student in self.students:
            if name.lower() in student.name.lower():
                result.append(student)
        return result 

    def search_by_department(self, department):
        result = []
        for student in self.students:
            if department.lower() in student.department.lower():
                result.append(student)
        return result
    
    def sort_by_gpa(self):
        return sorted(
            self.students,
            key = lambda student : student.gpa,
            reverse = True
        )

    def highest_gpa(self):
        if not self.students:
            return None
        return max(
            self.students,
            key = lambda student : student.gpa
        )        
          
    def lowest_gpa(self):
        if not self.students:
            return None
        return min(
            self.students,
            key = lambda student : student.gpa
        )       

    def average_gpa(self):
        if not self.students:
            return None
        total = 0
        for student in self.students:
            total += student.gpa 
        return round(total/ len(self.students) , 3)

    def statistics(self):
        if not self.students:
            return None
        
        total = len(self.students)
        highest = self.highest_gpa()
        lowest = self.lowest_gpa()
        average = self.average_gpa()

        return {
            "total students = "  : total, 
            "highest student : " : highest,
            "lowest student : " : lowest,
            "average students = " : average
        }

    def export_to_csv(self, filename="students.csv"):
         with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Student ID",
                "Name",
                "Age",
                "Department",
                "GPA"
            ])

            for student in self.students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.age,
                    student.department,
                    student.gpa
                ])
        