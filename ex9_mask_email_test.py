#Write a function mask_email that masks an email address, leaving only the first character of the username visible.
import re

def mask_email(email : str):
    regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,7}"  #r means raw string, so don't treat \ as escape characters. "\." means a "." because "." usually means any character in regex
    if not isinstance(email, str):
        return "Invalid Input"
    if not re.fullmatch(regex, email):
        return "Invalid Input"
    char = email[0]
    length = len(email)-1
    return char + ("*"*length)


def test_mask_email():
    result = mask_email("thisisanemail@gmail.com")
    expected = "t**********************"
    assert result == expected

def test_is_email_1():
    result = mask_email("This isn't an email")
    expected = "Invalid Input"
    assert result == expected

def test_is_email_2():
    result = mask_email("hello@hello@goodbye")
    expected = "Invalid Input"
    assert result == expected

def test_mask_email_not_str():
    result = mask_email(0)
    expected = "Invalid Input"
    assert result == expected

def test_mask_email_empty_str():
    result = mask_email("")
    expected = "Invalid Input"
    assert result == expected