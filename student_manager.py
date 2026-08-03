import json
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

    def save_students(self, filename = "students.json"):
        with open(filename, "w", encoding="utf-8") as file:
            data =[student.to_dict() for student in self.students]
            json.dump(data, file, indent = 4)

    def load_students(self, filename = "students.json"):
        try:
            with open(filename, "r") as file :
                 data = json.load(file)

                 self.students =[]
                 for i in data:
                    student = Student.from_dict(i)
                    self.students.append(student)
        except FileNotFoundError:
            self.students = []