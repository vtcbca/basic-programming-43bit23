def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {num_terms} terms: {list(fibonacci_generator(num_terms))}")
