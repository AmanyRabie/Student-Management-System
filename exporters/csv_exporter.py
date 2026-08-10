import csv


class CSVExporter:

    def export(self, students, filename="students.csv"):

        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student ID",
                "Name",
                "Age",
                "Department",
                "GPA"
            ])

            for student in students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.age,
                    student.department,
                    student.gpa
                ])