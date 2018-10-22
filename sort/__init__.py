"""
A module implementing a bunch of sort algorithms in Python.

"""

def _swap(i, j, l):
    """
    Helper function to swap elements i and j in list l.
    """
    l[i], l[j] = l[j], l[i]


from sort.bubble_sort import bubble_sort, recursive_bubble_sort
from sort.insertion_sort import insertion_sort, insertion_sort_
from sort.selection_sort import selection_sort

