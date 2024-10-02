#Q16. Remove First and last element of list
def remove_first_last(lst):
    if len(lst) <= 2:
        return []
    return lst[1:-1]

example_list = [1, 2, 3, 4, 5]
modified_list = remove_first_last(example_list)
print(modified_list)

