def cumulative_sum_of_lists_and_tuples(data):
    total = 0
    result = []

    for item in data:

        if isinstance(item, (list, tuple)):

            for num in item:
                total += num
                result.append(total)
        else:

            raise ValueError("All items must be lists or tuples containing numbers.")

    return result


data = [1, (2, 3), [4, 5], (6,), [7]]
cumulative_result = cumulative_sum_of_lists_and_tuples(data)
print(cumulative_result)
