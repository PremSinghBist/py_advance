# my_module.py
def calculate_total(prices, quantities):
    if len(prices) != len(quantities):
        raise ValueError("Lists must have the same length")
    return sum(p * q for p, q in zip(prices, quantities))
