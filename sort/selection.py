"""
Selection sort implementations.

https://www.geeksforgeeks.org/selection-sort/

"""

from sort import _swap


def selection_sort(unsorted):
    for curr_pos in range(len(unsorted)):
        for idx, value in enumerate(unsorted[curr_pos:]):
            if value < unsorted[curr_pos]:
                _swap(curr_pos, idx + curr_pos, unsorted)

    return unsorted
