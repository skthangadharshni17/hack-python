import re

def validate_cards():
    # Read the number of credit cards
    try:
        n = int(input())
    except EOFError:
        return
    pattern = re.compile(r"^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$")
    
    for _ in range(n):
        card = input().strip()
        # Check overall structure and hyphens
        if pattern.match(card):
            formatted_card = card.replace("-", "")
            if re.search(r"(\d)\1{3}", formatted_card):
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
validate_cards()
