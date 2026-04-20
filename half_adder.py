def half_adder(bit_a, bit_b):
    """
    Calculates the sum and carry of two bits.

    Args:
        bit_a: The first bit.
        bit_b: The second bit.

    Returns:
        A tuple containing the sum and carry.
    """
    sum_result = bit_a ^ bit_b  # XOR operation for sum
    carry = bit_a & bit_b      # AND operation for carry
    return sum_result, carry

# Example
a = 1
b = 0
sum_val, carry_val = half_adder(a, b)
print(f"Half Adder: Input a={a}, b={b}, Sum={sum_val}, Carry={carry_val}")
