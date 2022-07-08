"""List Utility Functions."""

__author__ = "730466575"


def only_evens(sample: list[int]) -> list[int]:
    """Return only even integers from a list."""
    evens: list[int] = []
    for item in sample:
        if item % 2 == 0:
            evens.append(item)
    return evens


def is_equal(first_list: list[int], second_list: list[int]) ->  bool:
    """Tests for list equality."""
    i: int = 0
    truth: bool = True
    if len(first_list) != len(second_list):
        return False
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            truth = False
        i += 1
    return truth


def sub(given: list[int], start: int, end: int) -> list[int]:
    """Return the subset of a given list."""
    subset: list[int] = []
    if len(given) == 0  or end <= 0:
        return subset
    if start < 0:
        start = 0
    if end >= len(given):
        end = -1
    i: int = start
    while i < end:
        subset.append(given[i])
        i += 1
        
    return subset

