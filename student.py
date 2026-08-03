class Student:
    def __init__(self, student_id, name, age, department, gpa):
        self.student_id = student_id
        self.name = name 
        self.age = age 
        self.department = department
        self.gpa = gpa 

    @property 
    def gpa(self):
        return self.__gpa

    @gpa.setter 
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value 
        else:
            raise ValueError("GPA must be bettween 0.0 and 4.0")
    
    def display_info(self):
        print(f"student ID : {self.student_id}")
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"department : {self.department}")
        print(f"GPA : {self.gpa}")

    def to_dict(self):
        return {
            "student_id" : self.student_id,
            "name" : self.name,
            "age" : self.age,
            "department" : self.department,
            "gpa" : self.gpa
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["department"],
            data["gpa"]
        )
