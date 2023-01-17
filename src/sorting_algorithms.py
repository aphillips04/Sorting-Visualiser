"""
This module contains the classes for all sorting algorithms.

Classes:
    Algorithm: Base class for all sorting algorithms.
    InsertionSort: Insertion sort algorithm.
    SelectionSort: Selection sort algorithm.
    MergeSort: Merge sort algorithm.
    QuickSort: Quick sort algorithm.
    HeapSort: Heap sort algorithm.
    RadixSort: Radix sort algorithm.
    CountingSort: Counting sort algorithm.
    ShellSort: Shell sort algorithm.
    TimSort: Tim sort algorithm.
"""
import random
import json


class Algorithm:
    """
    Base class for all sorting algorithms.

    Attributes:
        details: dict[str, str]
            A dictionary containing the name, time and space complexity of the algorithm.
        array: list[int]
            The array to be sorted.

    Methods:
        get_details(self, name: str) -> dict[str, str]
            Returns the details of the algorithm.
        print_details(self)
            Prints the details of the algorithm.
        generate_array(self) -> list[int]
            Generates a random array of integers to be sorted.
        sort(self)
            Placeholder for the sort method of individual algorithms.
        swap(self, index_1: int, index_2: int)
            Swaps the elements at the given indices.
    """
    __slots__ = "details", "array"

    def __init__(self, name: str):
        self.details: dict[str, str] = self.get_details(name)
        self.array = self.generate_array()

    def get_details(self, name: str) -> dict[str, str]:
        """Returns the details of the algorithm."""
        with open("src/algorithm_details.json", "r", encoding="UTF-8") as details:
            details = json.load(details)
        return {"Name": name, **details[name]}

    def print_details(self):
        """Prints the details of the algorithm."""
        print(f"Name: {self.details['Name']}")
        print(f"Time Complexity: {self.details['Time']}")
        print(f"Space Complexity: {self.details['Space']}")

    def generate_array(self) -> list[int]:
        """Generates a random array of integers to be sorted."""
        return [random.randint(0, 100) for _ in range(100)]

    def sort(self):
        """Placeholder for the sort method of individual algorithms."""

    def swap(self, array: list[int], index_1: int, index_2: int):
        """Swaps the elements at the given indices."""
        array[index_1], array[index_2] = array[index_2], array[index_1]


class InsertionSort(Algorithm):
    """
    Insertion sort algorithm.

    Methods:
        sort(self)
            Sorts the array using insertion sort.
    """

    def __init__(self):
        super().__init__("Insertion")

    def sort(self):
        """Sorts the array using insertion sort."""
        for top in range(1, len(self.array)):
            for current in range(top, 0, -1):
                if self.array[current - 1] < self.array[current]:
                    continue
                self.swap(self.array, current, current - 1)


class SelectionSort(Algorithm):
    """
    Selection sort algorithm.

    Methods:
        sort(self)
            Sorts the array using selection sort.
    """

    def __init__(self):
        super().__init__("Selection")

    def sort(self):
        """Sorts the array using selection sort."""
        for index in range(len(self.array) - 1):
            min_index = index
            for current in range(index + 1, len(self.array)):
                if self.array[current] < self.array[min_index]:
                    min_index = current
            if min_index != index:
                self.swap(self.array, index, min_index)


class MergeSort(Algorithm):
    """
    Merge sort algorithm.

    Methods:
        sort(self)
            Sorts the array using merge sort.
    """

    def __init__(self):
        super().__init__("Merge")

    def sort(self):
        """Sorts the array using merge sort."""
        self.array = self.merge_sort(self.array)

    def merge_sort(self, array: list[int]) -> list[int]:
        """Recursive implementation of merge sort."""
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        if len(left) > 1:
            left = self.merge_sort(left)

        if len(right) > 1:
            right = self.merge_sort(right)

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        """Merges two sorted arrays."""
        result: list[int] = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result


class QuickSort(Algorithm):
    """
    Quick sort algorithm.

    Methods:
        sort(self)
            Sorts the array using quick sort.
    """

    def __init__(self):
        super().__init__("Quick")

    def sort(self):
        """Sorts the array using quick sort."""
        self.array = self.quick_sort(self.array, 0, len(self.array) - 1)

    def quick_sort(self, array: list[int], low: int, high: int) -> list[int]:
        """Recursive implementation of quick sort."""
        if low < high:
            pivot = self.partition(array, low, high)
            self.quick_sort(array, low, pivot - 1)
            self.quick_sort(array, pivot + 1, high)

        return array

    def partition(self, array: list[int], low: int, high: int) -> int:
        """Partitions the array."""
        pivot = array[high]
        smaller = low - 1

        for current in range(low, high):
            if array[current] > pivot:
                continue
            smaller += 1
            self.swap(array, smaller, current)

        self.swap(array, smaller + 1, high)
        return smaller + 1


class HeapSort(Algorithm):
    """
    Heap sort algorithm.

    Methods:
        sort(self)
            Sorts the array using heap sort.
    """

    def __init__(self):
        super().__init__("Heap")

    def sort(self):
        """Sorts the array using heap sort."""


class RadixSort(Algorithm):
    """
    Radix sort algorithm.

    Methods:
        sort(self)
            Sorts the array using radix sort.
    """

    def __init__(self):
        super().__init__("Radix")

    def sort(self):
        """Sorts the array using radix sort."""


class CountingSort(Algorithm):
    """
    Counting sort algorithm.

    Methods:
        sort(self)
            Sorts the array using counting sort.
    """

    def __init__(self):
        super().__init__("Counting")

    def sort(self):
        """Sorts the array using counting sort."""
        unique_elements = max(self.array) + 1

        count = [0] * unique_elements
        for element in self.array:
            count[element] += 1

        for index in range(1, unique_elements):
            count[index] += count[index - 1]

        sorted_array = [0] * len(self.array)
        for element in self.array:
            sorted_array[count[element] - 1] = element
            count[element] -= 1

        self.array = sorted_array


class ShellSort(Algorithm):
    """
    Shell sort algorithm.

    Methods:
        sort(self)
            Sorts the array using shell sort.
    """

    def __init__(self):
        super().__init__("Shell")

    def sort(self):
        """Sorts the array using shell sort."""


class TimSort(Algorithm):
    """
    Tim sort algorithm.

    Methods:
        sort(self)
            Sorts the array using tim sort.
    """

    def __init__(self):
        super().__init__("TimSort")

    def sort(self):
        """Sorts the array using tim sort."""


def main():
    """Main function."""
    algorithms = [
        InsertionSort(),
        SelectionSort(),
        MergeSort(),
        QuickSort(),
        HeapSort(),
        RadixSort(),
        CountingSort(),
        ShellSort(),
        TimSort(),
    ]
    for algorithm in algorithms:
        try:
            algorithm.sort()
            assert algorithm.array == sorted(algorithm.array)
            algorithm.print_details()
            print()
        except AssertionError:
            print(f"{algorithm.details['Name']} sort failed!\n")


if __name__ == "__main__":
    main()
