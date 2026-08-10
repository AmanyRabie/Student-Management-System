from strategies.base_sort_strategy import BaseSortStrategy

class GPASortStrategy(BaseSortStrategy):
    def sort(self, students, reverse):
        if reverse:
            return sorted(
            students,
            key=lambda student: (
                -student.gpa,
                student.name.lower()
            )
        )
        return sorted(
            students,
            key=lambda student: (
                student.gpa,
                student.name.lower()
            )
        )
