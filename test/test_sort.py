import pytest
import random

from sort import bubble_sort

one_to_100 = list(range(1, 100))


def shuffle_list(input_list):
    new = list(input_list)
    random.shuffle(new)
    return new


@pytest.mark.parametrize('unsorted,expected', [
    (
        [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]
    ),
    (
        [4, 7, 2], [2, 4, 7]
    ),
    (
        shuffle_list(one_to_100), one_to_100
    )
])
def test_bubble_sort(unsorted, expected):
    assert expected == bubble_sort.bubble_sort(unsorted)


@pytest.mark.parametrize('unsorted,expected', [
    (
        [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]
    ),
    (
        [4, 7, 2], [2, 4, 7]
    ),
    (
        shuffle_list(one_to_100), one_to_100
    )
])
def test_recursive_bubble_sort(unsorted, expected):
    assert expected == bubble_sort.recursive_bubble_sort(unsorted)

