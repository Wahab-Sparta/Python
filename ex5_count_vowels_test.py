#Write a function count_vowels that counts the number of vowels in a string.

def count_vowels(words : str):
    if not isinstance(words, str):
        return "Invalid Input"
    vowels = ["a","e","i","o","u"]
    count = 0
    for char in words:
        if char in vowels:
            count = count + 1
    return count

def test_count_vowels_1():
    result = count_vowels("aeiou")
    expected = 5
    assert result == expected

def test_count_vowels_2():
    result = count_vowels("This is a sentence with some vowels")
    expected = 11
    assert result == expected

def test_count_vowels_none():
    result = count_vowels("Fly by my gym")
    expected = 0
    assert result == expected

def test_count_vowels_not_str():
    result = count_vowels(4)
    expected = "Invalid Input"
    assert result == expected

def test_count_vowels_empty_str():
    result = count_vowels("")
    expected = 0
    assert result == expected


