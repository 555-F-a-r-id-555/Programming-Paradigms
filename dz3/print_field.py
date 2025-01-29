import numpy as np
from dz3.constant import *

# Игровое поле
field = None

""" Инициализация игрового поля. """
def initialize():
    global field  # Используем глобальную переменную field
    field = np.full((FIELD_SIZE, FIELD_SIZE), DOT_EMPTY, dtype=object)
    return field  # Возвращаем инициализированное поле

""" Проверяет, находятся ли координаты в пределах игрового поля. """
def is_cell_valid(x, y):
    return 0 <= x < field_size_x and 0 <= y < field_size_y

""" Проверка, является ли ячейка игрового поля пустой. """
def is_cell_empty(x, y):
    return is_cell_valid(x, y) and field[x][y] == DOT_EMPTY

""" Вывод игрового поля в консоль. """
def print_field():
    print("  " + " ".join(f"{i+1}" for i in range(FIELD_SIZE)))  # Заголовок колонок
    print("  " + "-" * (FIELD_SIZE * 2))  # Верхняя линия

    for x in range(FIELD_SIZE):
        print(f"{x + 1}| " + " ".join(field[x]))  # Игровое поле

    print("  " + "-" * (FIELD_SIZE * 2))  # Нижняя линия

