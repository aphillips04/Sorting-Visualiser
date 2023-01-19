"""
This module contains the classes for all sorting algorithms.

Classes:
    Algorithm: Base class for all sorting algorithms.
    BubbleSort: Bubble sort algorithm.
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
        return {"Name": f"{name}{'' if (name.find('ort') != -1) else ' Sort'}", **details[name]}

    def print_details(self):
        """Prints the details of the algorithm."""
        print(f"Name: {self.details['Name']}")
        print(f"Time Complexity: {self.details['Time']}")
        print(f"Space Complexity: {self.details['Space']}")

    def generate_array(self) -> list[int]:
        """Generates a random array of integers to be sorted."""
        return [random.randint(0, 100) for _ in range(1000)]

    def sort(self):
        """Placeholder for the sort method of individual algorithms."""

    def swap(self, array: list[int], index_1: int, index_2: int):
        """Swaps the elements at the given indices."""
        array[index_1], array[index_2] = array[index_2], array[index_1]


class BubbleSort(Algorithm):
    """
    Bubble sort algorithm.

    Methods:
        sort(self)
            Sorts the array using bubble sort.
    """

    def __init__(self):
        super().__init__("Bubble")

    def sort(self):
        """Sorts the array using bubble sort."""
        for top in range(len(self.array) - 1, 0, -1):
            for current in range(top):
                if self.array[current] > self.array[current + 1]:
                    self.swap(self.array, current, current + 1)


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
        width = 1
        array_length = len(self.array)
        while width < array_length:
            for left in range(0, array_length, 2 * width):
                right = min(left + 2 * width - 1, array_length - 1)
                mid = min(left + width - 1, array_length - 1)
                self.merge(self.array, left, mid, right)
            width *= 2

    def merge(self, array: list[int], left: int, mid: int, right: int):
        """Merges the two sub-arrays of array"""
        length_1 = mid - left + 1
        length_2 = right - mid
        left_array = [0] * length_1
        right_array = [0] * length_2
        for index in range(length_1):
            left_array[index] = array[left + index]
        for index in range(length_2):
            right_array[index] = array[mid + index + 1]

        left_index, right_index, current_index = 0, 0, left
        while left_index < length_1 and right_index < length_2:
            if left_array[left_index] <= right_array[right_index]:
                array[current_index] = left_array[left_index]
                left_index += 1
            else:
                array[current_index] = right_array[right_index]
                right_index += 1
            current_index += 1

        while left_index < length_1:
            array[current_index] = left_array[left_index]
            left_index += 1
            current_index += 1

        while right_index < length_2:
            array[current_index] = right_array[right_index]
            right_index += 1
            current_index += 1


class QuickSort(Algorithm):
    """
    Quick sort algorithm.

    Methods:
        sort(self)
            Sorts the array using quick sort.
    """

    def __init__(self):
        super().__init__("Quicksort")

    def sort(self):
        """Sorts the array using quick sort."""
        stack = [0, len(self.array) - 1]

        while stack:
            high = stack.pop()
            low = stack.pop()

            pivot = self.partition(self.array, low, high)

            if pivot - 1 > low:
                stack.append(low)
                stack.append(pivot - 1)

            if pivot + 1 < high:
                stack.append(pivot + 1)
                stack.append(high)

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
        super().__init__("Heapsort")

    def sort(self):
        """Sorts the array using heap sort."""
        array_length = len(self.array)
        self.build_max_heap(array_length)

        for index in range(array_length - 1, 0, -1):
            self.swap(self.array, 0, index)

            heap_index = 0
            while True:
                left = 2 * heap_index + 1
                right = 2 * heap_index + 2

                if left >= index:
                    break

                if right >= index:
                    if self.array[left] > self.array[heap_index]:
                        self.swap(self.array, left, heap_index)
                    break

                if self.array[left] > self.array[right]:
                    if self.array[left] <= self.array[heap_index]:
                        break
                    self.swap(self.array, left, heap_index)
                    heap_index = left
                elif self.array[right] > self.array[heap_index]:
                    self.swap(self.array, right, heap_index)
                    heap_index = right
                else:
                    break

    def build_max_heap(self, array_length: int):
        """Builds the max heap."""
        for index in range(array_length):
            if self.array[index] > self.array[(index - 1) // 2]:
                swap = index
                while self.array[swap] > self.array[(swap - 1) // 2]:
                    self.swap(self.array, swap, (swap - 1) // 2)
                    swap = (swap - 1) // 2


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
        max_1 = max(self.array)

        exponent = 1
        while max_1 / exponent >= 1:
            self.counting_sort(exponent)
            exponent *= 10

    def counting_sort(self, exponent: int):
        """Sorts the array using counting sort."""
        length = len(self.array)
        output = [0] * length
        count = [0] * 10

        for current in range(length):
            index = self.array[current] // exponent
            count[index % 10] += 1

        for current in range(1, 10):
            count[current] += count[current - 1]

        current = length - 1
        while current >= 0:
            index = self.array[current] // exponent
            output[count[index % 10] - 1] = self.array[current]
            count[index % 10] -= 1
            current -= 1

        self.array = output


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
        super().__init__("Shellsort")

    def sort(self):
        """Sorts the array using shell sort."""
        length = len(self.array)
        gap = length // 2

        while gap > 0:
            index = gap
            while index < length:
                current = index - gap
                while current >= 0 and self.array[current] > self.array[current + gap]:
                    self.swap(self.array, current, current + gap)
                    current -= gap
                index += 1
            gap //= 2


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
        length = len(self.array)
        minimum_run = self.get_minimum_run(length)

        for start in range(0, length, minimum_run):
            end = min(start + minimum_run - 1, length - 1)
            self.insertion_sort(start, end)

        size = minimum_run
        while size < length:
            for left in range(0, length, 2 * size):
                mid = min(length - 1, left + size - 1)
                right = min(length - 1, left + 2 * size - 1)
                if mid < right:
                    self.merge(self.array, left, mid, right)
            size *= 2

    def get_minimum_run(self, length: int) -> int:
        """Gets the minimum run."""
        run = 0
        while length >= 64:
            run |= length & 1
            length >>= 1
        return length + run

    def insertion_sort(self, start: int, end: int):
        """Sorts the array using insertion sort."""
        for index in range(start + 1, end + 1):
            current = index - 1
            while current >= start and self.array[current] > self.array[current + 1]:
                self.swap(self.array, current, current + 1)
                current -= 1

    def merge(self, array: list[int], left: int, mid: int, right: int):
        """Merges the array."""
        length_1 = mid - left + 1
        length_2 = right - mid
        left_array = [0] * length_1
        right_array = [0] * length_2
        for index in range(length_1):
            left_array[index] = array[left + index]
        for index in range(length_2):
            right_array[index] = array[mid + index + 1]

        left_index, right_index, current_index = 0, 0, left
        while left_index < length_1 and right_index < length_2:
            if left_array[left_index] <= right_array[right_index]:
                array[current_index] = left_array[left_index]
                left_index += 1
            else:
                array[current_index] = right_array[right_index]
                right_index += 1
            current_index += 1

        while left_index < length_1:
            array[current_index] = left_array[left_index]
            left_index += 1
            current_index += 1

        while right_index < length_2:
            array[current_index] = right_array[right_index]
            right_index += 1
            current_index += 1


def main():
    """Main function."""
    algorithms = [
        BubbleSort(),       # Done
        InsertionSort(),    # Done
        SelectionSort(),    # Done
        MergeSort(),        # Done
        QuickSort(),        # Done
        HeapSort(),         # Done
        RadixSort(),        # Done
        CountingSort(),     # Done
        ShellSort(),
        TimSort(),
    ]
    for algorithm in algorithms:
        try:
            algorithm.sort()
            assert algorithm.array == sorted(algorithm.array)
            print(f"{algorithm.details['Name']}\n")
        except AssertionError:
            # print(f"{algorithm.details['Name']} sort failed!\n")
            pass


if __name__ == "__main__":
    main()
