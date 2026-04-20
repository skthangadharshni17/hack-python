def evaluate_boolean_expression(expression):
    # Evaluate the boolean expression
    return eval(expression)

if __name__ == "__main__":
    # Get user input for the boolean expression
    user_input = input("Enter a boolean expression (use 'and', 'or', 'not'): ")

    # Evaluate and print the result
    result = evaluate_boolean_expression(user_input)
    print(f"The result of the expression '{user_input}' is: {result}")