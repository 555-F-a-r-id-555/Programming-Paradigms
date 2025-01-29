import random
from dz3.check_win import check_win
from dz3.print_field import is_cell_empty, is_cell_valid
from dz3.constant import *

""" Ход игрока (человека) """
def human_turn(field, dot_human):
    if field is None:
        print("Ошибка: игровое поле не инициализировано!")
        return

    while True:
        try:
            x, y = map(int, input(f"Введите координаты хода X и Y\n(от 1 до {FIELD_SIZE}) через пробел: ").split())
            x -= 1
            y -= 1

            if not is_cell_valid(x, y):
                print(f"Координаты выходят за пределы поля (1-{FIELD_SIZE}). Попробуйте снова.")
                continue

            if not is_cell_empty(x, y):
                print("Эта клетка уже занята. Выберите другую.")
                continue

            field[x][y] = dot_human
            break

        except ValueError:
            print("Ошибка ввода! Введите два числа через пробел.")

""" Рандомный ход компьютера """
def ai_random_turn(field):
    while True:
        x = random.randint(0, FIELD_SIZE - 1)
        y = random.randint(0, FIELD_SIZE - 1)

        if is_cell_empty(x, y):
            field[x][y] = DOT_AI
            break

""" Осознанный ход компьютера """
def ai_turn(field, version_ai):
    if version_ai == 1:
        ai_random_turn(field)
    elif version_ai == 2:
        for steps_ahead in range(3):
            for i in range(FIELD_SIZE):
                for j in range(FIELD_SIZE):
                    if is_cell_empty(i, j):
                        field[i][j] = DOT_AI
                        if check_win(field,DOT_AI, steps_ahead):
                            return
                        field[i][j] = DOT_EMPTY

            for i in range(FIELD_SIZE):
                for j in range(FIELD_SIZE):
                    if is_cell_empty(i, j):
                        field[i][j] = DOT_HUMAN_X
                        if check_win(field,DOT_HUMAN_X, steps_ahead):
                            field[i][j] = DOT_AI
                            return
                        field[i][j] = DOT_EMPTY

        ai_random_turn(field)
