#Write a function is_even that returns True if a number is even otherwise False

def is_even(num: int):
    if not isinstance(num, int):
        return "Invalid Input"
    if num % 2 == 0:
        return True
    else:
        return False

def test_is_even():
    result = is_even(2)
    expected = True
    assert result == expected

def test_is_even_2():
    result = is_even(4)
    expected = True
    assert result == expected

def test_is_odd():
    result = is_even(3)
    expected = False
    assert result == expected

def test_is_odd_2():
    result = is_even(5)
    expected = False
    assert result == expected

def test_is_even_negative_num():
    result = is_even(-2)
    not_expected = True
    assert result == not_expected

def test_is_odd_negative_num():
    result = is_even(-1)
    not_expected = False
    assert result == not_expected

def test_is_even_not_int():
    result = is_even("test")
    expected = "Invalid Input"
    assert result == expected