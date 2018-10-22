"""
Implementations of the bubble sort algorithm.

https://www.geeksforgeeks.org/bubble-sort/

"""

from sort import _swap


def bubble_sort(unsorted):
    length = len(unsorted)
    for i in range(length):
        for idx in range(length - i - 1):
            if unsorted[idx] > unsorted[idx + 1]:
                _swap(idx, idx+1, unsorted)

    return unsorted


def recursive_bubble_sort(unsorted):
    for idx, num in enumerate(unsorted):
        try: 
            if unsorted[idx+1] < num:
                _swap(idx, idx + 1, unsorted)
                bubble_sort(unsorted)
        except IndexError: 
            pass

    return unsorted 