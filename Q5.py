# In a given list insert a number at given position


def insert_number(lst, number, position):

    if position < 0 or position > len(lst):
        print("Invalid position")
        return lst
    lst.insert(position, number)
    return lst

my_list = [1, 2, 3, 4, 5]
new_number = 10
position = 2
updated_list = insert_number(my_list, new_number, position)
print(updated_list)
