"""
Implementations of the bubble sort algorithm.

"""


def bubble_sort(unsorted):
    length = len(unsorted)
    for i in range(length):
        for idx in range(length - i - 1):
            if unsorted[idx] > unsorted[idx + 1]:
                unsorted[idx], unsorted[idx + 1] = unsorted[idx + 1], unsorted[idx]

    return unsorted


def recursive_bubble_sort(unsorted):
    for idx, num in enumerate(unsorted):
        try: 
            if unsorted[idx+1] < num:
                unsorted[idx], unsorted[idx + 1] = num, unsorted[idx + 1]
                bubble_sort(unsorted)
        except IndexError: 
            pass
    return unsorted 