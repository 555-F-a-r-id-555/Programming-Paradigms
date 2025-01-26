# Таблица умножения
# Домашнее задание
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит
# на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.


def multiply_function(n):
    j = 1
    i = 1
    while i < 10:
        while j <= n:
            res = (str(i) + " * " + str(j) + " = " + str(i * j) + " | " +
                   str(i + 1) + " * " + str(j) + " = " + str((i + 1) * j) + " | " +
                   str(i + 2) + " * " + str(j) + " = " + str((i + 2) * j) + " | ")
            j += 1
            print(res)
        print("---------------------------------------")
        j = 1
        i += 3


def multiply_function_v2(n):
    for i in range(1, 10, 3):
        for j in range(1, n + 1):
            res = " | ".join(
                f"{i + k} * {j} = {(i + k) * j}" for k in range(3) if i + k <= 9
            )
            print(res)
        print("-" * 40)



if __name__ == '__main__':
    multiply_function_v2(7)

    print("*" * 40)
    multiply_function(7)
