# #Write a function is_palindrome that returns True if the text is a palindrome.

def is_palindrome(text : str):
    if not isinstance(text, str):
        return "Invalid Input"
    text = text.lower()
    text = "".join(text.split()) #This will split the text into a list, removing the spaces, then joins the text with no spaces
    i = -1
    for char in text:
        if char != text[i]:
            return False
        else:
            i = i-1
        if i*-1 > len(text)/2:  #This is here to stop it doing more loops than it needs to. It will stop halfway through the text
            return True
    return True

def test_is_palindrome():
    result = is_palindrome("racecar")
    expected = True
    assert result == expected


def test_is_palindrome_caps():
    result = is_palindrome("Eva Can I See Bees In A Cave")
    expected = True
    assert result == expected


def test_is_not_palindrome():
    result = is_palindrome("This isn't a palindrome")
    expected = False
    assert result == expected



def test_is_palindrome_not_str():
    result = is_palindrome(["racecar"])
    expected = "Invalid Input"
    assert result == expected


