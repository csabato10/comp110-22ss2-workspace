"""Testing Utility Functions."""

__author__ = "730466575"

from utils import only_evens, is_equal, sub


def test_only_evens_zeros() -> None:
    """Tests list of same number for evens."""
    assert only_evens([2, 2, 2]) == [2, 2, 2]


def test_only_evens_mixed_values() -> None:
    """Tests list of mixed values for evens."""
    assert only_evens([2, 3, 4, 5, 7]) == [2, 4]


def test_only_evens_mixed_evens_and_odds() -> None:
    """Tests list of only odds."""
    assert only_evens([-2, -1, 0, 1, 2]) == [-2, 0, 2]


def test_is_equal_different_lengths() -> None:
    """Test is_equal with lists of different lengths."""
    AssertionError: is_equal([0, 1, 2], [1, 2])


def test_is_equal_equal() -> None:
    """Test is_equal with lists that are equal."""
    assert is_equal([0, 1, 2], [0, 1, 2]) == True


def test_is_equal_different() -> None:
    """Test is_equal with lists that are not equal."""
    assert is_equal([0, 1, 2], [3, 1, 2]) == False


def test_sub_full_list() -> None:
    """Test sub where full list is returned."""
    assert sub([1, 2, 3], 2, -1) == []


def test_sub_partial_list() -> None:
    """Test sub with a regular list."""
    assert sub([3, 4, 5], 1, 2) == [4]


def test_sub_regular_with_negative_start_greater_end() -> None:
    """Test sub with a negative start value and larger end."""
    assert sub([6, 7, 8, 9], -3, 5) == [6, 7, 8, 9]
