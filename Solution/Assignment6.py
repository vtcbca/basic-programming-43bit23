def star_pattern_list_comprehension(n):
    for i in range(1, n + 1):
        print(" ".join([ '*' for _ in range(i)]))

# Example usage
num_rows = int(input("Enter the number of rows: "))
star_pattern_list_comprehension(num_rows)
