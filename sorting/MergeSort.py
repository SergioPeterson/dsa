from math import floor as floor


class MergeSort:

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
        MergeSort algorithm
        """
        self._merge_sort(self._numbers, 0, len(self._numbers) - 1)
        return self._numbers

    def _merge_sort(self, numbers, l, r):
        
        if l < r:
            mid = floor((l + r) / 2)
            self._merge_sort(numbers, l, mid)
            self._merge_sort(numbers, mid + 1, r)
            self._merge(numbers, l, mid, r)    

    def _merge(self, numbers, l, mid, r):
        
        left_arr = []
        right_arr = []
        
        left_size = mid - l + 1
        right_size = r - mid 
 
        for i in range(0, left_size):
            left_arr.append(numbers[l + i])
        for j in range(0, right_size):
            right_arr.append(numbers[mid + j + 1])
        
        i = 0
        j = 0
        k = l

        while i != len(left_arr) and j != len(right_arr):
            if left_arr[i] <= right_arr[j]:
                numbers[k] = left_arr[i]
                i = i + 1
            else:
                numbers[k] = right_arr[j]
                j = j + 1
            k = k + 1

        if i < len(left_arr):
            while i != len(left_arr):
                numbers[k] = left_arr[i]
                i = i + 1
                k = k + 1
        if j < len(right_arr):
            while j != len(right_arr):
                numbers[k] = right_arr[j]
                j = j + 1
                k = k + 1


# MergeSort.py
