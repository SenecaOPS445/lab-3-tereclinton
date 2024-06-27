#!/usr/bin/env python3

# Define the list before the function definitions
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    """
    Appends a new item to the end of the list.
    The new item will be the last item's value plus one.
    """
    if ordered_list:  # Check if the list is not empty
        last_item = ordered_list[-1]
        ordered_list.append(last_item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    """
    Removes all values found in items_to_remove from the ordered_list.
    """
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)