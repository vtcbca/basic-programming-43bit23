def is_palindrome_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return s == reversed_str

# Example usage
input_str = input("Enter a string: ")
if is_palindrome_stack(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")
