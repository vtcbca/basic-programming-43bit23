def number_triangle_comprehension(n):
    for i in range(1, n + 1):
        # Create the list of numbers for this row and print with leading spaces
        print(" " * (n - i) + " ".join([str(x) for x in range(1, 2 * i)]))

# Example usage
num_lines = int(input("Enter the number of lines: "))
number_triangle_comprehension(num_lines)
