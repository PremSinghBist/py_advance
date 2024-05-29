# test_my_module.py

from src.my_module import calculate_total

def test_calculate_total_empty_lists():
    result = calculate_total([], [])
    assert result == 0

def test_calculate_total_same_length_lists():
    prices = [10, 20, 30]
    quantities = [2, 3, 1]
    result = calculate_total(prices, quantities)
    assert result == 10 * 2 + 20 * 3 + 30 * 1

def test_calculate_total_mismatched_lists():
    prices = [10, 20, 30]
    quantities = [2, 3]
    try:
        calculate_total(prices, quantities)
    except ValueError as e:
        assert str(e) == "Lists must have the same length"
    else:
        raise AssertionError("Expected ValueError")
