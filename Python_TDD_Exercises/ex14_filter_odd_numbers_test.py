#Write a function filter_odd_numbers that returns a new list containing only the odd numbers from a list.

def filter_odd_numbers(list_of_nums: list[int | float]):
    if not isinstance(list_of_nums, list):
        return "Invalid Input"
    if not list_of_nums:
        return "There are no numbers in the list"
    new_list = []
    for num in list_of_nums:
        if not isinstance(num, int):
            return 'Invalid Input'
        if num % 2 != 0:  # Checking remainder to see if odd
            new_list.append(num)

    if not new_list:  # Checking if list is empty
        return "There are no odd numbers in the list"

    return new_list


def test_filter_odd_numbers():
    result = filter_odd_numbers([1,2,3,4,5,6,7,8,9,10])
    expected = [1,3,5,7,9]
    assert result == expected

def test_filter_odd_numbers_odd_only():
    result = filter_odd_numbers([2,4,6,8,10])
    expected = "There are no odd numbers in the list"
    assert result == expected

def test_filter_odd_numbers_no_nums():
    result = filter_odd_numbers([])
    expected = "There are no numbers in the list"
    assert result == expected

def test_filter_odd_numbers_not_int():
    result = filter_odd_numbers(["these","are","not","numbers",True])
    expected = "Invalid Input"
    assert result == expected

def test_filter_odd_numbers_not_list():
    result = filter_odd_numbers("This isn't a list")
    expected = "Invalid Input"
    assert result == expected
