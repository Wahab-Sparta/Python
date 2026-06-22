#Write a function get_initials that returns the initials from a person's name

def get_initials(name : str):
    if not isinstance(name, str):
        return "Invalid input"
    split = name.split(" ")
    char = ""
    for name in split:
        char = char + name[0]
    return char

def test_get_initials_1():
    result = get_initials("John")
    expected = "J"
    assert result == expected

def test_get_initials_2():
    result = get_initials("John Doe")
    expected = "JD"
    assert result == expected

def test_get_initials_3():
    result = get_initials("John Doe Junior")
    expected = "JDJ"
    assert result == expected

def test_get_initials_not_string():
    result = get_initials(3)
    expected = "Invalid input"
    assert result == expected