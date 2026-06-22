#Write a function find_shortest_word that returns the shortest word from a list of strings.

def find_shortest_word(list_of_words : list[str]):
    if not isinstance(list_of_words, list):
        return "Invalid Input"
    if not list_of_words:
        return "There are no words in this list"
    if not isinstance(list_of_words[0], str):
        return "Invalid Input"
    shortest = list_of_words[0]
    for word in list_of_words:
        if not isinstance(word, str):
            return "Invalid Input"
        if len(shortest) > len(word):
            shortest = word
    if shortest == "":
        return "There are no words in this list"
    return shortest

def test_find_shortest_word():
    result = find_shortest_word(["evoke", "buffet", "finished", "poison", "identification"])
    expected = "evoke"
    assert result == expected

def test_find_shortest_word_same_length():
    result = find_shortest_word(["small", "clock", "bland", "title", "groan"])
    expected = "small"
    assert result == expected

def test_find_shortest_word_one_word():
    result = find_shortest_word(["small"])
    expected = "small"
    assert result == expected

def test_find_shortest_word_not_str():
    result = find_shortest_word([1, "buffet", "finished", "poison", "identification"])
    expected = "Invalid Input"
    assert result == expected

def test_find_shortest_word_not_list():
    result = find_shortest_word(3)
    expected = "Invalid Input"
    assert result == expected

def test_find_shortest_word_empty_list():
    result = find_shortest_word([])
    expected = "There are no words in this list"
    assert result == expected

def test_find_shortest_word_empty_str():
    result = find_shortest_word(["","",""])
    expected = "There are no words in this list"
    assert result == expected