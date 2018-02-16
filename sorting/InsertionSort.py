

class InsertionSort:

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
        naive insertion sort
        """
        l = len(self._numbers)
        for i in range(1, l):
            current = self._numbers[i]
            j = i - 1
            while j >= 0 and current < self._numbers[j]:
                self._numbers[j + 1] = self._numbers[j]
                j = j - 1
            self._numbers[j + 1] = current
        return self._numbers

# InsertionSort.py
