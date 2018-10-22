import pytest
import random

from sort import bubble_sort, recursive_bubble_sort, insertion_sort_, insertion_sort, selection_sort

one_to_100 = list(range(1, 100))


def shuffled(input_list):
    new = list(input_list)
    random.shuffle(new)
    return new


sort_test_cases = [
    [],
    [1, 2, 3, 4, 5, 6],
    [2, 4, 7, 7, 10],
    one_to_100,
    one_to_100
]


@pytest.mark.parametrize('expected', sort_test_cases)
def test_bubble_sort(expected):
    assert expected == bubble_sort(shuffled(expected))


@pytest.mark.parametrize('expected', sort_test_cases)
def test_recursive_bubble_sort(expected):
    assert expected == recursive_bubble_sort(shuffled(expected))


@pytest.mark.parametrize('expected', sort_test_cases)
def test_insertion_sort_impl1(expected):
    assert expected == insertion_sort(shuffled(expected))


@pytest.mark.parametrize('expected', sort_test_cases)
def test_insertion_sort_impl2(expected):
    assert expected == insertion_sort_(shuffled(expected))


