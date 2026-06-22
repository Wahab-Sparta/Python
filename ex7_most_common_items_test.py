#Write a function most_common_item that returns the most common item in a list.

def most_common_item(items : list):
    if not isinstance(items, list):
        return "Invalid Input"
    if not items:
        return "List is empty"
    count_dict = {}
    for item in items:  #Puts all items in a dictionary where it has counted how many times an item appears in the list
        if item in count_dict:
            count_dict[item] = count_dict[item] + 1
        else:
            count_dict[item] = 1
    common = max(count_dict, key=lambda k: count_dict[k]) #A lambda function can take any number of arguments, but can only have one expression.
    return common                                         #I'm just using lambda to look through the dictionary's values instead of keys

def test_most_common_item():
    result = most_common_item([3,1,1,3,"word","word","3", 1])
    expected = 1
    assert result == expected

def test_most_common_item_not_list():
    result = most_common_item("This is not a list")
    expected = "Invalid Input"
    assert result == expected

def test_most_common_item_empty_list():
    result = most_common_item([])
    expected = "List is empty"
    assert result == expected



