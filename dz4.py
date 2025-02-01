import random



def random_array(n: int) -> list:
    return [random.randint(0, 10) for _ in range(n)]


def average_value(lst: list) -> float:
    return sum(lst) / len(lst)


def deviation_from_the_mean(value: float, average_val: float) -> float:
    return value - average_val


def list_deviation(lst: list) -> list:
    avg_val = average_value(lst)
    return [deviation_from_the_mean(x, avg_val) for x in lst]


def numerator(list_x: list, list_y: list) -> float:
    return sum(x * y for x, y in zip(list_x, list_y))


def denominator(list_x: list, list_y: list) -> float:
    return (sum(x ** 2 for x in list_x) ** 0.5) * (sum(y ** 2 for y in list_y) ** 0.5)


def pearson_correlation(num: int) -> float:
    list_x = random_array(num)
    list_y = random_array(num)

    list_deviation_x = list_deviation(list_x)
    list_deviation_y = list_deviation(list_y)

    denom = denominator(list_deviation_x, list_deviation_y)
    return numerator(list_deviation_x, list_deviation_y) / denom if denom != 0 else 0


print(pearson_correlation(10))




# def random_array(n: int) -> list:
#     return list(map(lambda x: random.randint(0, 10), range(n)))
#
#
# def average_value(lst: list) -> float:
#     return sum(lst) / len(lst)
#
# def deviation_from_the_mean(value: int, average_val: float) -> float:
#     return value - average_val
#
# def list_deviation(num: int) -> list:
#     rand_array = random_array(num)
#     return list(map(lambda xy: deviation_from_the_mean(xy, average_value(rand_array)), rand_array))
#
#
# def numerator(list_x: list, list_y: list) -> float:
#     return sum(list(map(lambda x, y: x * y, list_x, list_y)))
#
#
# def denominator(list_x: list, list_y: list) -> float:
#     return sum(list(map(lambda x, y: x ** 2 * y ** 2, list_x, list_y))) ** 0.5
#
#
# def pearson_correlations(num: int) -> float:
#     list_deviation_x = list_deviation(num)
#     list_deviation_y = list_deviation(num)
#     return numerator(list_deviation_x, list_deviation_y) / denominator(list_deviation_x, list_deviation_y)
#
#
# print(pearson_correlations(10))