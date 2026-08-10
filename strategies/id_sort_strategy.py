from strategies.base_sort_strategy import BaseSortStrategy

class IDSortStrategy(BaseSortStrategy):
    def sort(self, students, reverse):
        return sorted(
            students,
            key = lambda student : student.student_id,
            reverse= reverse
        )