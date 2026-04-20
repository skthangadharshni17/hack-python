def fibonacci(n, mode='iterative'):
    if mode == 'iterative':
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    elif mode == 'recursive':
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1, mode) + fibonacci(n - 2, mode)
    else:
        raise ValueError("Mode must be 'iterative' or 'recursive'.")

# Example usage
n = int(input("Enter the position in Fibonacci sequence (non-negative integer): "))
mode = input("Enter mode ('iterative' or 'recursive'): ").strip().lower()

try:
    result = fibonacci(n, mode)
    print(f"The {n}th Fibonacci number using {mode} mode is: {result}")
except ValueError as e:
    print(e)