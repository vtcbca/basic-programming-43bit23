def factorial_list_comprehension(n):
    return 1 if n == 0 else [x for x in range(1, n + 1)].reduce(lambda x, y: x * y)

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial_list_comprehension(num)}")
