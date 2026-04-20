
def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b

if __name__ == "__main__":
    # Define inputs
    a = True
    b = False

    print(f"AND({a}, {b}) = {AND(a, b)}")
    print(f"OR({a}, {b}) = {OR(a, b)}")
    print(f"NOT({a}) = {NOT(a)}")
    print(f"NAND({a}, {b}) = {NAND(a, b)}")
    print(f"NOR({a}, {b}) = {NOR(a, b)}")
    print(f"XOR({a}, {b}) = {XOR(a, b)}")
    print(f"XNOR({a}, {b}) = {XNOR(a, b)}")
