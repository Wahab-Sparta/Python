#Write a function count_words that returns a dictionary showing how many times each word appears in a sentence.

def count_words(words : list[str]):
    if not isinstance(words, list):
        return "Invalid Input"
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return count_dict

def test_count_words():
    result = count_words(["cafe", "stretch", "vertical", "vertical", "stretch", "cafe", "functional", "functional", "stretch", "affair", "functional", "cafe", "stretch"])
    expected = {"cafe" : 3, "stretch" : 4, "vertical" : 2, "functional" : 3, "affair" : 1}
    assert result == expected

def test_count_words_empty_list():
    result = count_words([])
    expected = {}
    assert result == expected

def test_count_words_not_str():
    result = count_words(22)
    expected = "Invalid Input"
    assert result == expected

def test_count_words_not_list():
    result = count_words("This is not a list")
    expected = "Invalid Input"
    assert result == expected

