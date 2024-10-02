def right_justify(string, width):
    return string.rjust(width)

# Example usage
input_string = "Hello"
justified_string = right_justify(input_string, 10)
print(justified_string)  # Output: "     Hello"
