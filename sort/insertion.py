"""
Insertion sort implementations.

https://www.geeksforgeeks.org/insertion-sort/

"""


def insertion_sort(unsorted):
    """
    Implementation of insertion sort.
    """

    for idx in range(1, len(unsorted)):
        key = unsorted[idx]
        search_idx = idx - 1

        while search_idx >= 0 and key < unsorted[search_idx]:
            unsorted[search_idx + 1] = unsorted[search_idx]
            search_idx -= 1

        unsorted[search_idx + 1] = key

    return unsorted


def insertion_sort_(unsorted):
    """
    Implementation of insertion sort, where instead of "shifting" the list's elements,
    we pop the element out and then put it into the list at the right place.

    """
    final = list(unsorted)

    for idx in range(1, len(final)):
        if final[idx] < final[idx - 1]:
            value = final.pop(idx)
            for i, val in enumerate(final):
                if val >= value:
                    final.insert(i, value)
                    break

    return final

