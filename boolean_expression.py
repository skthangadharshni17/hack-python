def evaluate_boolean_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

if __name__ == "__main__":

    expression = input("Enter a boolean expression (use 'and', 'or', 'not'): ")
    result = evaluate_boolean_expression(expression)
    print(f"The result of the expression '{expression}' is: {result}")