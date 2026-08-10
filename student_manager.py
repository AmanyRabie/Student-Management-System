from student import Student
from repositories.json_student_repository import JSONStudentRepository

class StudentManager:
    def __init__(self):
        self.repository = JSONStudentRepository()
        self.students = self.repository.load()

    def add_student(self, student):
         # student => object from class student 
        for s in self.students :
            if s.student_id == student.student_id:
                raise ValueError("Student ID already exists.")
        self.students.append(student)
        self.repository.save(self.students)

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def remove_student(self, student_id):
        student = self.find_student(student_id)
        if student: 
             self.students.remove(student)
             self.repository.save(self.students)
        else:
             raise ValueError("Student not found.")

    def update_gpa(self, student_id, new_gpa):
        student = self.find_student(student_id)
        if student:
            student.gpa = new_gpa
            self.repository.save(self.students)
        else:
             raise ValueError("Student not found.")

    def get_all_students(self):
         return self.students

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
        
    def advanced_filter(
        self,
        name = None,
        department = None,
        min_gpa = None,
        max_gpa = None,
        min_age = None,
        max_age = None
    ):
        result = []
        for student in self.students:
            if name and name.lower() not in student.name.lower():
                continue
            if department and department.lower() not in student.department.lower():
                continue
            if min_gpa is not None and student.gpa < min_gpa:
                continue
            if max_gpa is not None and student.gpa > max_gpa:
                continue
            if min_age is not None and student.age < min_age:
                continue
            if max_age is not None and student.age > max_age:
                continue

            result.append(student)
        return result 