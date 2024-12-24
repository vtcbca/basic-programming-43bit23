def print_alphabet_row(n, i=1):
    if i > n:
        return
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print increasing alphabet sequence
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")

    # Print decreasing alphabet sequence
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end=" ")
    
    print()  # Move to next line
    
    print_alphabet_row(n, i + 1)

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_alphabet_row(num_lines)
