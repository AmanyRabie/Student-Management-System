# Student Management System

A Python-based Student Management System developed as a learning project to practice **Object-Oriented Programming, Design Patterns, Clean Code, and Software Architecture**.


##  Current Version

**Version: 3.0**

V3 focuses on improving the system's architecture and introducing reusable design patterns.


##  Features

### Student Management

* Add a new student
* Remove a student
* Find a student by ID
* Update student GPA
* Display all students

### Search

* Search students by name
* Search students by department

### Statistics

* Total number of students
* Highest GPA student
* Lowest GPA student
* Average GPA

### Advanced Filtering

Students can be filtered using multiple criteria:

* Name
* Department
* Minimum GPA
* Maximum GPA
* Minimum Age
* Maximum Age

Multiple filters can be combined in the same search.

### Advanced Sorting

The system supports multiple sorting strategies:

* Sort by GPA
* Sort by Name
* Sort by Age
* Sort by Student ID

Each sorting method supports:

* Ascending order
* Descending order

When students have the same GPA, they are sorted alphabetically by name.

### Data Export

* Export students to CSV
* Student data is stored in JSON format



##  Design Patterns

### Command Pattern

The Command Pattern is used to encapsulate user actions into independent command classes.

Examples:

AddStudentCommand
RemoveStudentCommand
FindStudentCommand
UpdateGPACommand
DisplayAllStudentCommand
SearchByNameCommand
SearchByDepartmentCommand
StudentStatisticsCommand
ExportToCSVCommand
AdvancedFilterCommand
AdvancedSortCommand
ExitCommand


This reduces the large number of `if/elif` statements previously used in the main program.


### Strategy Pattern

The Strategy Pattern is used for Advanced Sorting.
Available strategies:
GPASortStrategy
NameSortStrategy
AgeSortStrategy
IDSortStrategy


The sorting algorithm can be changed without modifying `StudentManager`.


##  Project Architecture

student-management-system/
│
├── main.py
├── student.py
├── student_manager.py
├── students.json
├── students.csv
│
├── commands/
│   ├── base_command.py
│   ├── add_student_command.py
│   ├── remove_student_command.py
│   ├── find_student_command.py
│   ├── update_gpa_command.py
│   ├── display_all_student_command.py
│   ├── exit_command.py
│   ├── search_by_name_command.py
│   ├── search_by_department_command.py
│   ├── student_statistics_command.py
│   ├── export_to_csv_command.py
│   ├── advanced_filter_command.py
│   └── advanced_sort_command.py
│
├── strategies/
│   ├── base_sort_strategy.py
│   ├── gpa_sort_strategy.py
│   ├── name_sort_strategy.py
│   ├── age_sort_strategy.py
│   └── id_sort_strategy.py
│
├── exporters/
│   └── csv_exporter.py
│
└── repositories/
    └── json_student_repository.py


---

## Data Storage

Student data is stored in:
students.json


The system also supports exporting student information to:
students.csv


The JSON storage logic has been separated from `StudentManager` using a dedicated repository class.

---

##  Refactoring in V3

Version 3 introduced several architectural improvements:

* Separated commands from business logic
* Introduced Command Pattern
* Introduced Strategy Pattern
* Removed the old dedicated GPA sorting command
* Added Advanced Sorting
* Added Advanced Filtering
* Added Ascending/Descending sorting
* Added secondary alphabetical sorting for equal GPAs
* Separated CSV exporting into `CSVExporter`
* Separated JSON persistence into `JSONStudentRepository`
* Separated display responsibility from `StudentManager`
* Improved separation of concerns

---

##  Technologies

* Python 3
* Object-Oriented Programming
* JSON
* CSV
* Git & GitHub
* Design Patterns

---

## ▶️ How to Run

Clone the repository and navigate to the project directory:

```bash
cd student-management-system
```

Run the application:

```bash
python main.py
```

---

##  Version History

### V1.0

* Basic Student Management System
* OOP implementation
* JSON persistence
* CRUD operations

### V2.0

* Student search
* Department search
* GPA sorting
* Student statistics
* CSV export

### V3.0

* Command Pattern
* Strategy Pattern
* Advanced Filtering
* Advanced Sorting
* Ascending / Descending sorting
* Secondary sorting
* CSV Exporter
* JSON Repository
* Refactoring and separation of responsibilities

### V4.0 — Planned

Planned improvements:

* Repository Abstraction
* BaseRepository
* SQLite Database
* Dependency Injection
* Better Error Handling
* Configuration Management
* Unit Testing
* Further architectural improvements

---

##  Project Goal

The goal of this project is not only to build a functional Student Management System, but also to gradually transform it into a **clean, maintainable, scalable, and well-structured Python application** while learning professional software development practices.


Amany Rabie