
class BubbleSort:

    def __init__(self, numbers):
        """
        Constructor resposible to initialize the list of numbers

        Args:
            param1: The list of numbers to be sorted

        """
        self._numbers = []
        if isinstance(numbers, list):
            self._numbers = numbers

    def sort(self):
        """
        legendary bubble sort - classic version
        """
        l = len(self._numbers)
        for i in range(0, l):
            for j in range(i + 1, l):
                if self._numbers[i] >= self._numbers[j]:
                    self._swap(i, j)
        return self._numbers

    def _swap(self, i, j):
        temp = self._numbers[i]
        self._numbers[i] = self._numbers[j]
        self._numbers[j] = temp

# BubbleSort.py
