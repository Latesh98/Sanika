#Invert the dictionary
def invert_dict(d):
    inverted = {}

    for key, value in d.items():

        if value in inverted:
            if not isinstance(inverted[value], list):
                inverted[value] = [inverted[value]]
            inverted[value].append(key)
        else:
            inverted[value] = key

    return inverted

original_dict = {'a': 1, 'b': 2, 'c': 1}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)

