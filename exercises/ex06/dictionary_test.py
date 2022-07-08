"""Test functions in dictionary."""

from dictionary import invert
from exercises.ex06.dictionary import invert, favorite_color, count
import pytest

def test_invert_double_key() -> None:
    """Test invert function dictionary with two identical values."""
    with pytest.raises(KeyError):
        a = {"string": "bean", "pinto": "bean"}
        invert(a)

def test_invert_normal_dictionary() -> None:
    """Test invert function with single letters."""
    assert invert({"z": "a", "y": "b"}) == {"a": "z", "b": "y"}


def test_invert_dictionary_of_names() -> None:
    """Test invert function with first and last names."""
    assert invert({"James": "Bond", "Harrison": "Ford"}) == {"Bond": "James", "Ford": "Harrison"}


def test_all_different_colors() -> None:
    """Test of all the same colors."""
    colors = {"Karl": "orange", "Daniel": "red", "James": "purple"}
    assert favorite_color(colors) == "orange"


def test_tie_colors() -> None:
    """Test for a tie in colors."""
    colors = {"Karl": "purple", "Daniel": "orange", "James": "purple", "Blake": "orange"}
    assert favorite_color(colors) == "purple"


def test_singal_popular_colors():
    """Test for a single popular color."""
    colors = {"Karl": "red", "Daniel": "red", "James": "purple"}
    assert favorite_color(colors) == "red"


def test_all_different_count():
    """Test of list different values."""
    classes = ["math", "science", "english"]
    assert count(classes) == {"math": 1, "science": 1, "english": 1}


def test_repeated_classes_count():
    """Test for repeated values in list."""
    classes = ["math", "science", "english", "science"]
    assert count(classes) == {"math": 1, "science": 2, "english": 1}


def test_no_classes_count():
    """Test for empty list."""
    classes = []
    assert count(classes) == {}