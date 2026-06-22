#Write a function grade_score that converts a numeric score into a grade.
#For this function the grade score is capped at 100

def grade_score(score):
    if not isinstance(score, (int, float)):
        return "Invalid Input"
    if score < 0 or score > 100:
        return "Invalid Input. Your grade score is over 100 or below 0"
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def test_grade_score_aplus():
    result_1 = grade_score(100)
    result_2 = grade_score(90)
    expected = "A+"
    assert result_1 == expected
    assert result_2 == expected

def test_grade_score_a():
    result_1 = grade_score(89)
    result_2 = grade_score(80)
    expected = "A"
    assert result_1 == expected
    assert result_2 == expected

def test_grade_score_b():
    result_1 = grade_score(79)
    result_2 = grade_score(70)
    expected = "B"
    assert result_1 == expected
    assert result_2 == expected

def test_grade_score_c():
    result_1 = grade_score(69)
    result_2 = grade_score(60)
    expected = "C"
    assert result_1 == expected
    assert result_2 == expected

def test_grade_score_d():
    result_1 = grade_score(59)
    result_2 = grade_score(50)
    expected = "D"
    assert result_1 == expected
    assert result_2 == expected

def test_grade_score_f():
    result_1 = grade_score(40)
    result_2 = grade_score(0)
    expected = "F"
    assert result_1 == expected
    assert result_2 == expected

def test_grade_score_not_int_float():
    result = grade_score("76")
    expected = "Invalid Input"
    assert result == expected

def test_grade_score_bounds_1():
    result = grade_score(101)
    expected = "Invalid Input. Your grade score is over 100 or below 0"
    assert result == expected

def test_grade_score_bounds_2():
    result = grade_score(-1)
    expected = "Invalid Input. Your grade score is over 100 or below 0"
    assert result == expected
