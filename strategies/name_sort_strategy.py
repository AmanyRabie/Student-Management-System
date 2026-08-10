from strategies.base_sort_strategy import BaseSortStrategy

class NameSortStrategy(BaseSortStrategy):
    def sort(self, students, reverse):
        return sorted(
            students,
            key=lambda student: student.name.lower(),
            reverse= reverse
        )