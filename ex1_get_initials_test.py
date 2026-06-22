#Write a function get_initials that returns the initials from a person's name

def get_initials(name : str):
    if not isinstance(name, str):
        return "Invalid input"
    if name == "":
        return "Empty string"
    split = name.split(" ")
    char = ""
    for name in split:
        if name == "":
            return "Empty string"
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

def test_get_initials_not_str():
    result = get_initials(3)
    expected = "Invalid input"
    assert result == expected

def test_get_initials_empty_str():
    result = get_initials("")
    expected = "Empty string"
    assert result == expected

def test_get_initials_whitespace_str():
    result = get_initials(" ")
    expected = "Empty string"
    assert result == expected
