#Write a function count_passes_and_fails that returns the number of passing and failing scores in a list.

def count_passes_and_fails(scores : list[int | float]):
    if not isinstance(scores, list):
        return "Invalid Input"
    if not scores:
        return "Scores list is empty"
    count = 0
    passing = 50
    for score in scores:
        if not isinstance(score, int | float):
            return "Invalid Input"
        if score < 0:
            return "A score is below 0"
        if score >= passing:
            count = count + 1
    return count


def test_count_passes_and_fails():
    result = count_passes_and_fails([0, 12, 25, 33.5, 49.5, 50, 67.5, 73, 84, 94, 103])
    expected = 6
    assert result == expected

def test_count_passes_and_fails_empty_list():
    result = count_passes_and_fails([])
    expected = "Scores list is empty"
    assert result == expected

def test_count_passes_and_fails_not_int_or_float():
    result = count_passes_and_fails(["these","aren't","scores"])
    expected = "Invalid Input"
    assert result == expected

def test_count_passes_and_fails_below_0():
    result = count_passes_and_fails([0, 12, 25, 33, -1, 50, 67, 73, 84, 94, 103])
    expected = "A score is below 0"
    assert result == expected
