# Author: Thomas Monfre
# Date: 11/1/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program sorts the information in world_cities.txt using quicksort and partition algorithms

# returns boolean evaluating whether or not a given value is less than or equal to a second given value
def comparison_function(func_type, x, y):
    return func_type(x, y)

# given a list, starting and ending indices (p,r) and a function used to compare values, determine a pivot index and
# rearrange values in the list such that all values before the pivot are less than pivot, and all values after are
# greater than the pivot
def partition(list, p, r, comparison_function_type):
    # i is the index of the last element before where the pivot value will be inserted
    i = p - 1
    # j is the index of the first element after where the pivot value will be inserted
    j = p
    # pivot is set to the value of the last element in the list
    pivot = list[r]

    # for all elements in the list, determine whether or not the currently examined index j should be moved in the list
    # and do so if necessary
    while j <= r:
        # move the currently examined index to the end of the section of elements before where pivot will be placed
        # if the value is less than or equal to pivot
        if comparison_function(comparison_function_type, list[j], pivot):
            # advance the index of the last element in the list before where pivot will be inserted
            i = i + 1

            # swap the elements at index i and index j
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

        # advance the element being looked at
        j = j + 1

    return i

# given a list, starting and ending indices (p,r) and a function used to compare values, recursively sort the list
def quicksort(list, p, r, comparison_function_type):
    if p < r:
        index = partition(list, p, r, comparison_function_type)
        quicksort(list, p, index - 1, comparison_function_type)
        quicksort(list, index + 1, r, comparison_function_type)

# given a list and a function for evaluating comparing the type of data in it, sort the list
def sort(list, comparison_function_type):
    quicksort(list, 0, len(list) - 1, comparison_function_type)
