import pytest

from sort import bubble_sort


@pytest.mark.parametrize('unsorted,expected', [
    (
        [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6]
    ),
    (
        [4, 7, 2], [2, 4, 7]
    )
])
def test_bubble_sort(unsorted, expected):
    assert expected == bubble_sort.bubble_sort(unsorted)