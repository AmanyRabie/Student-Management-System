from abc import ABC, abstractmethod

class BaseSortStrategy:
    @abstractmethod
    def sort(self, Students, reverse = False) : #asc
        pass
