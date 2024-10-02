#10. Write a function to check whether dictionary has duplicates

def has_duplicate_values(input_dict):
    values = list(input_dict.values())
    return len(values) != len(set(values))

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 1}
print(has_duplicate_values(my_dict))

another_dict = {'x': 1, 'y': 2, 'z': 3}
print(has_duplicate_values(another_dict))
