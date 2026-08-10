from strategies.base_sort_strategy import BaseSortStrategy

class AgeSortStrategy(BaseSortStrategy):
    def sort(self, students, reverse):
        return sorted(
            students,
            key = lambda  student : student.age,
            reverse= reverse
        )