"""
Ваша задача:
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


def binary_search(num_list, n, count=0):
    if not num_list:
        return -1

    middlle = len(num_list) // 2
    left_half = num_list[:middlle]
    right_half = num_list[middlle + 1:]

    if num_list[middlle] == n:
        return count + middlle
    elif num_list[middlle] > n:
        return binary_search(left_half, n, count)
    else:
        return binary_search(right_half, n, count + middlle + 1)


num_array1 = [77, 2, 3, 4, 5, 60, 70, 1]
num_array1.sort()
print(num_array1)
print(f"Поиск {1}: {binary_search(num_array1, 1)}")
print("Поиск 2: ",binary_search(num_array1, 2))
print("Поиск 3: ",binary_search(num_array1, 3))
print("Поиск 4: ",binary_search(num_array1, 4))
print("Поиск 5: ",binary_search(num_array1, 5))
print("Поиск 60: ",binary_search(num_array1, 60))
print("Поиск 70: ",binary_search(num_array1, 70))
print("Поиск 77: ",binary_search(num_array1, 77))
print("Поиск 770: ",binary_search(num_array1, 770))

num_array2 =[]
print(num_array2)
print("Поиск 100: ",binary_search(num_array2,100))


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


num_array3 = [60, 2, 3, 4, 5, 1, 70, 77]
num_array3.sort()
print(num_array3)
print("Поиск 5: ",binary_search_imperative(num_array3, 5))
print("Поиск 60: ",binary_search_imperative(num_array3, 60))
print("Поиск 77: ",binary_search_imperative(num_array3, 77))
print("Поиск 100: ",binary_search_imperative(num_array3, 100))



# def binary_search(num_list, n, count=0):
#     if len(num_list) == 1 and num_list[0] != n:
#         return -1
#
#     middlle = len(num_list) // 2
#     left_half = num_list[:middlle]
#     right_half = num_list[middlle:]
#
#     if num_list[middlle] > n:
#         return binary_search(left_half, n, count)
#     elif num_list[middlle] < n:
#         return binary_search(right_half, n, count + middlle)
#     else:
#         return count + middlle


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