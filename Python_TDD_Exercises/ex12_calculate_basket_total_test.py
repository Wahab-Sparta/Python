#Write a function calculate_basket_total that calculates the total cost of a shopping basket from a list of items, prices, and quantities.
#{"item" : "", "price" : , "quantity" : },
def calculate_basket_total(basket : list[dict[str, str | float | int]]):
    if not isinstance(basket, list):    #Checks if basket is a list
        return "Invalid Input"
    if not basket:                      #Checks is basket is empty
        return "Your basket is empty (list)"
    if not isinstance(basket[0], dict): #Checks if the dict in the basket is a dict
        return "Invalid Input"
    if len(basket[0]) == 0:             #Checks if the dict in the basket is empty
        return "Your basket is empty (dict)"
    total = 0

    for item in basket:
        if not isinstance(item, dict):  #Checks if the dict is a dict
            return "Invalid Input"
        if not isinstance(item["item"], str):   #Checks if the item is a string
            return "Invalid Input. Item in basket is not a string"
        if not isinstance(item["price"], (int,float)):  #Checks if the price is an int or float
            return "Invalid Input. Price in basket is not an int or float"
        if not isinstance(item["quantity"], int):   #Checks if the quantity is an int
            return "Invalid Input. Quantity in basket is not an int"
        if item["quantity"] < 0:        #Checks if the quantity is below 0
            return "Invalid Input. Your quantity for one or more items is below 0"
        total = total + (item["price"] * item["quantity"])
    return round(total, 2)


def test_calculate_basket_total():
    result = calculate_basket_total([{"item" : "Bread", "price" : 1.80, "quantity" : 2}, {"item" : "Cheese", "price" : 3.40 , "quantity" : 1 }, {"item" : "Bananas", "price" : 0.30 , "quantity" : 6 }, {"item" : "Orange Juice", "price" : 2.20 , "quantity" : 2 }, {"item" : "Eggs", "price" : 3.10 , "quantity" : 2 }])
    expected = 19.40    #(1.8*2)+3.4+(0.3*6)+(2.2*2)+(3.10*2)
    assert result == expected

def test_calculate_basket_total_negative_quantity():
    result = calculate_basket_total([{"item" : "Bread", "price" : 1.80, "quantity" : 1}, {"item" : "Cheese", "price" : 3.40 , "quantity" : -1 }, {"item" : "Bananas", "price" : 0.30 , "quantity" : 6 }, {"item" : "Orange Juice", "price" : 2.20 , "quantity" : 2 }, {"item" : "Eggs", "price" : 3.10 , "quantity" : 2 }])
    expected = "Invalid Input. Your quantity for one or more items is below 0"
    assert result == expected

def test_calculate_basket_total_not_list_or_dict():
    result_1 = calculate_basket_total("cheese")
    result_2 = calculate_basket_total({"item" : "Bread", "price" : 1.80, "quantity" : 1})
    result_3 = calculate_basket_total([{"item" : "Bread", "price" : 1.80, "quantity" : 1}, "cheese"])
    expected = "Invalid Input"
    assert result_1 == expected
    assert result_2 == expected
    assert result_3 == expected

def test_calculate_basket_total_empty_list():
    result = calculate_basket_total([])
    expected = "Your basket is empty (list)"
    assert result == expected

def test_calculate_basket_total_empty_dict():
    result = calculate_basket_total([{}])
    expected = "Your basket is empty (dict)"
    assert result == expected

def test_calculate_basket_total_item_not_str():
    result = calculate_basket_total([{"item" : 2, "price" : 1.80, "quantity" : 2}])
    expected = "Invalid Input. Item in basket is not a string"
    assert result == expected

def test_calculate_basket_total_price_not_int_or_float():
    result = calculate_basket_total([{"item" : "Bread", "price" : "1.80", "quantity" : 2}])
    expected = "Invalid Input. Price in basket is not an int or float"
    assert result == expected

def test_calculate_basket_total_quantity_not_int():
    result = calculate_basket_total([{"item" : "Bread", "price" : 1.80 , "quantity" : "2"}])
    expected = "Invalid Input. Quantity in basket is not an int"
    assert result == expected