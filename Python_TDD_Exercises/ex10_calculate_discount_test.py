#Write a function calculate_discount that calculates a discounted price given a price and discount percentage.

def calculate_discount(price : int | float, discount : int | float):
    if not isinstance(price, (int, float)) or not isinstance(discount, (int,float)):
        return "Invalid Input"
    if discount > 100:
        return "Invalid Input. Your discount is over 100%"
    if price < 1 or discount < 1:
        return "Invalid Input. Your price or discount is 0 or below"
    return round(price * discount/100, 2)

def test_calculate_discount():
    result = calculate_discount(100, 50)
    expected = 50
    assert result == expected

def test_calculate_discount_float():
    result = calculate_discount(350.99, 37.5)
    expected = 131.62
    assert result == expected

def test_calculate_discount_over_100():
    result = calculate_discount(100, 150)
    expected = "Invalid Input. Your discount is over 100%"
    assert result == expected

def test_calculate_discount_price_0():
    result = calculate_discount(0, 50)
    expected = "Invalid Input. Your price or discount is 0 or below"
    assert result == expected

def test_calculate_discount_discount_0():
    result = calculate_discount(100, 0)
    expected = "Invalid Input. Your price or discount is 0 or below"
    assert result == expected

def test_calculate_discount_negative_num():
    result = calculate_discount(-100, 50)
    expected = "Invalid Input. Your price or discount is 0 or below"
    assert result == expected

def test_calculate_discount_negative_num_2():
    result = calculate_discount(100, -50)
    expected = "Invalid Input. Your price or discount is 0 or below"
    assert result == expected

def test_calculate_not_int_float():
    result = calculate_discount("not a price", "not a discount")
    expected = "Invalid Input"
    assert result == expected