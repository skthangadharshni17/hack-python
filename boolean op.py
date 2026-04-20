def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XNOR(a, b):
    return OR(AND(a, b), AND(NOT(a), NOT(b)))

# Example usage
if __name__ == "__main__":
    inputs = [(False, False), (False, True), (True, False), (True, True)]
    for a, b in inputs:
        result = XNOR(a, b)
        print(f"XNOR({a}, {b}) = {result}")