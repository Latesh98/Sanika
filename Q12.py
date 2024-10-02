#Computes the sum of all numbers in a list of lists.

def sum_of_lists(lst_of_lists):
    total_sum = 0

    for sublist in lst_of_lists:

        total_sum += sum(sublist)

    return total_sum

data = [[1, 2, 3], [4, 5], [6]]
total = sum_of_lists(data)
print(total)
