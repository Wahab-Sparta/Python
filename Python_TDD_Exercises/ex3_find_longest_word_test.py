#Write a function find_longest_word that returns the longest word from a list of strings.

def find_longest_word(list_of_words : list[str]):
    if not isinstance(list_of_words, list):
        return "Invalid Input"
    if not list_of_words:
        return "There are no words in this list"
    longest = ""
    for word in list_of_words:
        if not isinstance(word, str):
            return "Invalid Input"
        if len(longest) < len(word):
            longest = word
    if longest == "":
        return "There are no words in this list"
    return longest

def test_find_longest_word():
    result = find_longest_word(["evoke", "buffet", "finished", "poison", "identification"])
    expected = "identification"
    assert result == expected

def test_find_longest_word_same_length():
    result = find_longest_word(["small", "clock", "bland", "title", "groan"])
    expected = "small"
    assert result == expected

def test_find_longest_word_one_word():
    result = find_longest_word(["small"])
    expected = "small"
    assert result == expected

def test_find_longest_word_not_str():
    result = find_longest_word([1, "buffet", "finished", "poison", "identification"])
    expected = "Invalid Input"
    assert result == expected

def test_find_longest_word_not_list():
    result = find_longest_word(3)
    expected = "Invalid Input"
    assert result == expected

def test_find_longest_word_empty_list():
    result = find_longest_word([])
    expected = "There are no words in this list"
    assert result == expected

def test_find_longest_word_empty_str():
    result = find_longest_word(["","",""])
    expected = "There are no words in this list"
    assert result == expected