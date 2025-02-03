"""
Ваша задача:
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


def binary_search(num_list, n, count=0):
    if len(num_list) == 1 and num_list[0] != n:
        return -1

    middlle = len(num_list) // 2
    left_half = num_list[:middlle]
    right_half = num_list[middlle:]

    if num_list[middlle] > n:
        return binary_search(left_half, n, count)
    elif num_list[middlle] < n:
        return binary_search(right_half, n, count + middlle)
    else:
        return count + middlle


# num_array = [1, 2, 3, 4, 5, 60, 70, 77]
# print(binary_search(num_array, 1))
# print(binary_search(num_array, 2))
# print(binary_search(num_array, 3))
# print(binary_search(num_array, 4))
# print(binary_search(num_array, 5))
# print(binary_search(num_array, 60))
# print(binary_search(num_array, 70))
# print(binary_search(num_array, 77))
# print(binary_search(num_array, 770))

# num_array2 = []
# print(binary_search(num_array2, 1))  # IndexError: list index out of range



def binary_search_imperative(num_list, n):
    left, right = 0, len(num_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if num_list[middle] == n:
            return middle
        elif num_list[middle] < n:
            left = middle + 1
        else:
            right = middle - 1

    return -1


num_array = [1, 2, 3, 4, 5, 60, 70, 77]
print(binary_search_imperative(num_array, 5))
print(binary_search_imperative(num_array, 60))
print(binary_search_imperative(num_array, 77))
print(binary_search_imperative(num_array, 100))