def full_adder(a, b, carry_in):
    # Sum is XOR of inputs and carry_in
    sum_ = (a ^ b) ^ carry_in
    # Carry out is majority of the inputs
    carry_out = (a & b) | (b & carry_in) | (a & carry_in)
    return sum_, carry_out

def full_subtractor(a, b, borrow_in):
    # Difference is XOR of inputs and borrow_in
    diff = (a ^ b) ^ borrow_in
    # Borrow out when a borrow is needed
    borrow_out = ((not a) & b) | ((not (a ^ b)) & borrow_in)
    # Convert boolean to int (0 or 1)
    borrow_out = int(borrow_out)
    return diff, borrow_out

# Example usage
if __name__ == "__main__":
    # Inputs (bits): 0 or 1
    a, b, carry_in, borrow_in = 1, 1, 0, 0

    sum_, carry_out = full_adder(a, b, carry_in)
    print(f"Full Adder: a={a}, b={b}, carry_in={carry_in} => sum={sum_}, carry_out={carry_out}")

    diff, borrow_out = full_subtractor(a, b, borrow_in)
    print(f"Full Subtractor: a={a}, b={b}, borrow_in={borrow_in} => diff={diff}, borrow_out={borrow_out}")