# Exercise 1
# Check if the given list is sorted (from smallest to greatest)
def is_sorted(list):
    # To be implemented
    return False

# ====================================================

# Exercise 2
# Swap the values on the selected two indexes in the given list.
def swap(list, idx1, idx2):
    # To be implemented
    pass

# ====================================================

# Exercise 3
# Finds the greatest difference between two neighbour indexes.
def greatest_neighbour_difference(list):
    # To be implemented
    return 0

# ====================================================

# Exercise 4
# Find the index of the maximum value in the list
def index_of_max(list):
    # To be implemented
    return -1

# ====================================================

# Exercise 5
# Reverse the given list and return it.
def reverse_list(list):
    # To be implemented
    return list

# ====================================================

# Exercise 6
# Find the common elements between two lists.
def common_elements(list1, list2):
    # To be implemented
    return list1

# ====================================================

# Exercise 7
# Count how many times a given element appears in the list.
def count_element(list, element):
    # To be implemented
    return -1

# ====================================================

# Exercise 8
# Given a list, return a new list where each element is doubled.
def double_elements(list):
    # To be implemented
    return list


if __name__ == '__main__':
    print("Exercise 1")
    print(is_sorted([1, 2, 5, 9]))  # True
    print(is_sorted([1, 7, 5, 9]))  # False

    print('\n====================================================\n')

    print("Exercise 2")
    swap([1, 3, 2, 6, 7, 5], 0, 2)  # [2, 3, 1, 6, 7, 5]
    swap([1, 3, 2, 6, 7, 5], 3, 4)  # [1, 3, 2, 7, 6, 5]

    print('\n====================================================\n')

    print("Exercise 3")
    print(greatest_neighbour_difference([1, 2, 5, 6, 7]))  # 3
    print(greatest_neighbour_difference([1, 3, 6, 10, 11, 13, 4, 6, 5]))  # 9

    print('\n====================================================\n')

    print("Exercise 4")
    print(index_of_max([1, 2, 5, 6, 3]))  # 2

    print('\n====================================================\n')

    print("Exercise 5")
    print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]

    print('\n====================================================\n')

    print("Exercise 6")
    print(common_elements([1, 2, 3], [2, 3, 4]))  # [2, 3]

    print('\n====================================================\n')

    print("Exercise 7")
    print(count_element([1, 2, 2, 3, 4, 2], 2))  # 3
