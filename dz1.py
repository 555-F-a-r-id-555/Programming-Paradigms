# Задача №1
# Дан список целых чисел numbers.
# Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.


def buble_sort_imperative_v1(arr):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                not_sorted = True
    return arr


def buble_sort_imperative_v2(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort_imperative_v1(arr):
    for j in range(len(arr)):
        max_index = j
        for i in range(j + 1, len(arr), 1):
            if arr[max_index] < arr[i]:
                max_index = i
        arr[j], arr[max_index] = arr[max_index], arr[j]
    return arr


def insertion_sort_imperative(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def sort_lict_declarative(arr):
    return sorted(arr, reverse=True)

if __name__ == '__main__':

    print("buble_sort_imperative_v1 = " +
          str(buble_sort_imperative_v1([10, 20, 50, 90, 80, 30, 40, 50])))
    print("#" * 50)

    print("buble_sort_imperative_v2 = " +
          str(buble_sort_imperative_v2([10, 20, 50, 90, 80, 30, 40, 50])))

    print("#" * 50)
    print("selection_sort_imperative_v1 = " +
          str(selection_sort_imperative_v1([10, 20, 50, 90, 80, 30, 40, 50])))

    print("#" * 50)
    print("insertion_sort_imperative_v1 = " +
          str(insertion_sort_imperative([10, 20, 50, 90, 80, 30, 40, 50])))

    print("#" * 50)
    print("sort_list_declarative = " +
          str(sort_lict_declarative([10, 20, 50, 90, 80, 30, 40, 50])))