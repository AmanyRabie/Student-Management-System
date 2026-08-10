import json
import os

from student import Student


class JSONStudentRepository:

    def __init__(self, filename="students.json"):
        self.filename = filename

    def save(self, students):
        filepath = os.path.join(
            os.path.dirname(__file__),
            "..",
            self.filename
        )
        with open(filepath, "w", encoding="utf-8") as file:
            data = [student.to_dict() for student in students]

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

            
    def load(self):
        filepath = os.path.join(
            os.path.dirname(__file__),
            "..",
            self.filename
        )
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

            return [
                Student.from_dict(item)
                for item in data
            ]
        except FileNotFoundError:
            return []