

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
        sorted_numbers = []
        for n in self._numbers:
            pos = 0
            l = len(sorted_numbers) - 1
            while l >= 0:
                if sorted_numbers[l] < n:
                    pos = l + 1
                l = l - 1
            sorted_numbers.insert(pos, n)
        return sorted_numbers
