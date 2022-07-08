"""Functions to practice dictionary manipulation."""

from multiprocessing.sharedctypes import Value


def invert(original: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in original:
        if original[key] in inverted:
            raise KeyError("Key Error")
        inverted[original[key]] = key
    return inverted

def favorite_color(survey: dict[str, str]) -> str:
    votes: dict[str, int] = {}
    tracker: int = 0
    color: str = ""
    for key in survey:
        if survey[key] in votes:
            votes[survey[key]] = votes[survey[key]] + 1
        else:
            votes[survey[key]] = 1
    i: int = 0
    for value in votes:
        if votes[value] > i:
            i = votes[value]
            color = value
    return color


def count(given: list[str]) -> dict[str, int]:
    count: dict[str, int] = {}
    for value in given:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    return count
