# Крестики-нолики
# ● Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера


import random

import numpy as np


# Константы
DOT_EMPTY = '*'
DOT_HUMAN_X = 'X'
DOT_HUMAN_O = '0'
DOT_AI = '0'
FIELD_SIZE = 5
field_size_x = 5
field_size_y = 5

# Игровое поле
field = None


""" Инициализация игрового поля. """
def initialize():
    global field  # Используем глобальную переменную field
    field = np.full((FIELD_SIZE, FIELD_SIZE), DOT_EMPTY, dtype=object)


""" Проверяет, находятся ли координаты в пределах игрового поля. """
def is_cell_valid(x, y):
    return 0 <= x < field_size_x and 0 <= y < field_size_y


""" Проверка, является ли ячейка игрового поля пустой."""
def is_cell_empty(x, y):
    return is_cell_valid(x, y) and field[x][y] == DOT_EMPTY
    # return field[x][y] == DOT_EMPTY


""" Вывод игрового поля в консоль. """
def print_field():
    print("  " + " ".join(f"{i+1}" for i in range(FIELD_SIZE)))  # Заголовок колонок
    print("  " + "-" * (FIELD_SIZE * 2))  # Верхняя линия

    for x in range(FIELD_SIZE):
        print(f"{x + 1}| " + " ".join(field[x]))  # Игровое поле

    print("  " + "-" * (FIELD_SIZE * 2))  # Нижняя линия

    # print("+", end=' ')
    # for x in range(field_size_x):
    #     print(f"- {x + 1}", end=' ')
    # print("-")
    #
    # for x in range(field_size_x):
    #     print(f"{x + 1} |", end=" ")
    #     for y in range(field_size_y):
    #         print(f"{field[x][y]} |", end=" ")  # Вывод значения из массива field
    #     print()
    #
    # # Отображение нижней линии таблицы
    # for x in range(field_size_x * 2 + 2):
    #     print("-", end=" ")
    # print()


""" Ход игрока (человека) """
def human_turn(dot_human):
    if field is None:
        print("Ошибка: игровое поле не инициализировано!")
        return

    while True:
        try:
            x, y = map(int, input(f"Введите координаты хода X и Y\n(от 1 до {FIELD_SIZE}) через пробел: ").split())
            x -= 1  # Преобразуем в индексы массива
            y -= 1

            if not is_cell_valid(x, y):
                print(f"Координаты выходят за пределы поля (1-{FIELD_SIZE}). Попробуйте снова.")
                continue

            if not is_cell_empty(x, y):
                print("Эта клетка уже занята. Выберите другую.")
                continue

            field[x][y] = dot_human
            break  # Завершаем цикл после успешного хода

        except ValueError:
            print("Ошибка ввода! Введите два числа через пробел.")


""" Рандомный ход компьютера"""
def ai_random_turn():
    while True:
        x = random.randint(0, FIELD_SIZE - 1)  # Генерируем случайное X
        y = random.randint(0, FIELD_SIZE - 1)  # Генерируем случайное Y

        if is_cell_empty(x, y):  # Проверяем, свободна ли ячейка
            field[x][y] = DOT_AI  # Делаем ход
            break

""" Осознанный ход компьютера """
def ai_turn(version_ai):
    match version_ai:
        case 1:
            ai_random_turn()

        case 2:
            for steps_ahead in range(3):  # Проверка на 1-2 хода вперед
                # Проверка победы AI в следующих ходах
                for i in range(FIELD_SIZE):
                    for j in range(FIELD_SIZE):
                        if is_cell_empty(i, j):
                            field[i][j] = DOT_AI
                            if check_win(DOT_AI, steps_ahead):
                                return  # Если AI победит, ход уже сделан
                            field[i][j] = DOT_EMPTY  # Откатываем ход

                # Блокировка победы игрока
                for i in range(FIELD_SIZE):
                    for j in range(FIELD_SIZE):
                        if is_cell_empty(i, j):
                            field[i][j] = DOT_HUMAN_X
                            if check_win(DOT_HUMAN_X, steps_ahead):
                                field[i][j] = DOT_AI  # Если игрок победит, блокируем ход
                                return
                            field[i][j] = DOT_EMPTY  # Откатываем ход

            # Если нет выигрышного или блокирующего хода, делаем случайный ход
            ai_random_turn()

        case _:
            print("Ошибка! Введите 1 или 2.")
            return ai_turn(version_ai)  # Повторный запрос на ввод при ошибке


# def ai_turn():
#     try:
#         version_ai = int(input("Введите версию AI (1 — случайный, 2 — умный): "))
#     except ValueError:
#         print("Ошибка ввода! Введите число 1 или 2.")
#         return ai_turn()
#
#     match version_ai:
#         case 1:
#             ai_random_turn()
#
#         case 2:
#             for steps_ahead in range(3):  # Проверка на 1-2 хода вперед
#                 # Проверка победы AI в следующих ходах
#                 for i in range(FIELD_SIZE):
#                     for j in range(FIELD_SIZE):
#                         if is_cell_empty(i, j):
#                             field[i][j] = DOT_AI
#                             if check_win(DOT_AI, steps_ahead):
#                                 return  # Если AI победит, ход уже сделан
#                             field[i][j] = DOT_EMPTY  # Откатываем ход
#
#                 # Блокировка победы игрока
#                 for i in range(FIELD_SIZE):
#                     for j in range(FIELD_SIZE):
#                         if is_cell_empty(i, j):
#                             field[i][j] = DOT_HUMAN_X
#                             if check_win(DOT_HUMAN_X, steps_ahead):
#                                 field[i][j] = DOT_AI  # Если игрок победит, блокируем ход
#                                 return
#                             field[i][j] = DOT_EMPTY  # Откатываем ход
#
#             # Если нет выигрышного или блокирующего хода, делаем случайный ход
#             ai_random_turn()
#
#         case _:
#             print("Ошибка! Введите 1 или 2.")
#             return ai_turn()

# def ai_turn(version_ai):
#     match input("Введите версию Ai: "):
#         case 1:
#             ai_random_turn()
#         case 2:
#             for n in range(3): # число 3 - проверка на 1 и 2 хода вперед
#             # Проверка победы AI в следующем ходу
#                 for  i in range( field_size_x):
#                     for j in range(field_size_y):
#                         if is_cell_empty(i, j):
#                             field[i][j] = DOT_AI
#                             if check_win(DOT_AI, n):
#                                 field[i][j] = DOT_AI # Если AI победит, делаем ход
#                                 return
#                             field[i][j] = DOT_EMPTY
#
#
#             # Блокирование победы игрока в следующем ходу
#             for i in range(field_size_x):
#                 for j in range(field_size_y):
#                     if is_cell_empty(i, j):
#                         field[i][j] = DOT_HUMAN_X
#                         if check_win(DOT_HUMAN_X, n):
#                             field[i][j] = DOT_AI # Если игрок победит, блокируем его ход
#                             return
#                         field[i][j] = DOT_EMPTY
#
#
#     # Если нет выигрышного или блокирующего хода, делаем случайный ход
#     ai_random_turn()


# Проверка на ничью


def check_draw():
    """ Проверяет, есть ли на поле свободные клетки. """
    return not any(DOT_EMPTY in row for row in field)

# def check_draw():
#     for x in range(field_size_x):
#         for y in range(field_size_y):
#             if is_cell_empty(x, y): return False
#     return True


""" Метод проверки победы 
 @param dot фишка игрока
 Проверка победы
"""
# def check_win(dot):
#     steps_ahead = 0
#     return check_win_diagonal(dot, steps_ahead) or check_win_horizontal_vertical(dot, steps_ahead)
#
# # Проверка победы по диагонали
# def check_win_diagonal(dot, steps_ahead):
#     count_main_diagonal = 0
#     count_anti_diagonal = 0
#     i = 0
#     j = 0
#     for k in range(field_size_x):
#         if i + k < field_size_x and j + k < field_size_y and field[i + k][j + k] == dot:
#             count_main_diagonal += 1
#             if count_main_diagonal == field_size_x - steps_ahead:
#                 return True
#         if i + k < field_size_x and j - k >= 0 and field[i + k][j - k] == dot:
#             count_anti_diagonal += 1
#             if count_anti_diagonal == field_size_y - steps_ahead:
#                 return True
#     return False
#
# # Проверка победы по горизонтали и вертикали
# def check_win_horizontal_vertical(dot, steps_ahead):
#     for i in range(field_size_x):
#         counter_x = 0
#         counter_y = 0
#         for j in range(field_size_y):
#             if field[i][j] == dot:
#                 counter_x += 1
#             if field[j][i] == dot:
#                 counter_y += 1
#         if counter_x == field_size_x - steps_ahead or counter_y == field_size_y - steps_ahead:
#             return True
#     return False

def check_win(dot, steps_ahead=0):
    """ Проверяет, может ли игрок с заданной фишкой выиграть за `steps_ahead` ходов. """
    win_length = FIELD_SIZE - steps_ahead  # Количество фишек, необходимых для победы
    return check_win_diagonal(dot, win_length) or check_win_horizontal_vertical(dot, win_length)


def check_win_diagonal(dot, win_length):
    """ Проверяет победу по двум диагоналям. """
    # Главная диагональ (↘)
    for start in range(FIELD_SIZE - win_length + 1):
        if all(field[start + i][start + i] == dot for i in range(win_length)):
            return True

    # Побочная диагональ (↙)
    for start in range(FIELD_SIZE - win_length + 1):
        if all(field[start + i][FIELD_SIZE - 1 - (start + i)] == dot for i in range(win_length)):
            return True

    return False


def check_win_horizontal_vertical(dot, win_length):
    """ Проверяет победу по горизонтали и вертикали. """
    for i in range(FIELD_SIZE):
        # Проверка строк (—)
        for start in range(FIELD_SIZE - win_length + 1):
            if all(field[i][start + j] == dot for j in range(win_length)):
                return True
        # Проверка столбцов (|)
        for start in range(FIELD_SIZE - win_length + 1):
            if all(field[start + j][i] == dot for j in range(win_length)):
                return True

    return False


""" Проверяет текущее состояние игры (победа, ничья или продолжаем). """
def check_state(dot, win_message, steps_ahead=0):
    if check_win(dot, steps_ahead):
        print(win_message)
        return True
    if check_draw():
        print("Ничья!")
        return True
    return False  # Игра продолжается

# def check_state(dot, s):
#     if check_win(dot):
#         print(s)
#         return True
#     elif check_draw():
#         print("Ничья!")
#         return True
#     return False  # Игра продолжается


# def coop_game():
#     while True:
#         initialize()
#         print_field()
#         while True:
#             print("Ход первого игрока")
#             human_turn(DOT_HUMAN_X)
#             print_field()
#             if check_state(DOT_HUMAN_X, "Игрок 'X' победил!"):
#                 break
#             print("Ход второго игрока")
#             human_turn(DOT_HUMAN_O)
#             print_field()
#             if check_state(DOT_HUMAN_O, "Игрок '0' победил!"):
#                 break
#         # Запрос на новую игру
#         if not play_again():
#             break
#
#
# def solo_game():
#     while True:
#         try:
#             print("Введите уровень сложности: \n" +
#                   "1) Ai random\n" +
#                   "2) Ai immortal\n")
#             version_ai = int(input())
#
#             if version_ai not in [1, 2]:  # Проверка на правильность ввода
#                 print("Ошибка! Пожалуйста, выберите 1 или 2.")
#                 continue
#         except ValueError:
#             print("Ошибка! Введите число.")
#             continue
#
#         initialize()
#         print_field()
#         while True:
#             human_turn(DOT_HUMAN_X)
#             print_field()
#             if check_state(DOT_HUMAN_X, "Вы победили!"):
#                 break
#             ai_turn(version_ai)
#             print_field()
#             if check_state(DOT_AI, "Победил компьютер!"):
#                 break
#         # Запрос на новую игру
#         if not play_again():
#             break

def coop_game():
    while True:
        initialize()
        print_field()
        while True:
            print("Ход первого игрока")
            human_turn(DOT_HUMAN_X)
            print_field()
            if check_state(DOT_HUMAN_X, "Игрок 'X' победил!"):
                break
            print("Ход второго игрока")
            human_turn(DOT_HUMAN_O)
            print_field()
            if check_state(DOT_HUMAN_O, "Игрок '0' победил!"):
                break
        # Запрос на новую игру
        if not play_again():
            break


def solo_game():
    while True:
        try:
            print("Введите уровень сложности: \n"
                  "1) Ai random\n"
                  "2) Ai immortal\n")
            version_ai = int(input())

            if version_ai not in [1, 2]:  # Проверка на правильность ввода
                print("Ошибка! Пожалуйста, выберите 1 или 2.")
                continue
        except ValueError:
            print("Ошибка! Введите число.")
            continue

        initialize()
        print_field()
        while True:
            human_turn(DOT_HUMAN_X)
            print_field()
            if check_state(DOT_HUMAN_X, "Вы победили!"):
                break
            ai_turn(version_ai)
            print_field()
            if check_state(DOT_AI, "Победил компьютер!"):
                break
        # Запрос на новую игру
        if not play_again():
            break


def play_again():
    return input("Желаете сыграть еще раз? (Y - да): ").strip().lower() == "y"

# def play_again():
#     print("Желаете сыграть еще раз? (Y - да): ")
#     return input().strip().lower() == "y"

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Введите число: "))
            if user_choice not in [1, 2]:
                print("Ошибка! Введите 1 или 2.")
                continue
            return user_choice
        except ValueError:
            print("Ошибка ввода! Введите число.")


if __name__ == '__main__':
    print("Выберите режим:"
          "\n1 - coop"
          "\n2 - solo")

    user_choice = get_user_choice()

    match user_choice:
        case 1:
            coop_game()
        case 2:
            solo_game()



# if __name__ == '__main__':
#     print("Выберите режим:"
#           "\n1 - coop"
#           "\n2 - solo")
#
#     while True:
#         try:
#             user_choice = int(input("Введите число: "))
#         except ValueError:
#             print("Ошибка ввода! Введите число.")
#             continue
#
#         match user_choice:
#             case 1:
#                 coop_game()
#                 break  # Выход после завершения игры
#             case 2:
#                 solo_game()
#                 break  # Выход после завершения игры
#             case _:
#                 print("Вводить можно только числа:"
#                       "\n1 - coop game"
#                       "\n2 - solo game")





# def coop_game():
#     while True:
#         initialize()
#         print_field()
#         while True:
#             print("Ход первого игрока")
#             human_turn(DOT_HUMAN_X)
#             print_field()
#             if check_state(DOT_HUMAN_X, "Игрок 'X' победил!"):
#                 break
#             print("Ход второго игрока")
#             human_turn(DOT_HUMAN_O)
#             print_field()
#             if check_state(DOT_HUMAN_O, "Игрок '0' победил!"):
#                 break
#         # Запрос на новую игру
#         print("Желаете сыграть еще раз? (Y - да): ")
#         if input().strip().lower() != "y":  # Проверка ввода
#             break
#
#
# def solo_game():
#     print("Введите уровень сложности: \n" +
#                        "1) Ai random - 2 \n" +
#                        "2) Ai immortal - 3\n")
#     version_ai = int(input())
#     while True:
#         initialize()
#         print_field()
#         while True:
#             human_turn(DOT_HUMAN_X)
#             print_field()
#             if check_state(DOT_HUMAN_X, "Вы победили!"):
#                 break
#             ai_turn(version_ai)
#             print_field()
#             if check_state(DOT_AI, "Победил компьютер!"):
#                 break
#         # Запрос на новую игру
#         print("Желаете сыграть еще раз? (Y - да): ")
#         if input().strip().lower() != "y":  # Проверка ввода
#             break




# if __name__ == '__main__':
#     res = True
#     print("Выберите режим:"
#           " 1 - coop "
#           " 2 - solo")
#     while res:
#         match int(input("Введите число: ")):
#             case 1:
#                 res = False
#                 coop_game()
#             case 2:
#                 res = False
#                 solo_game()
#             case default:
#                 print("Вводить можно только числа: "
#                       "1 - coop game "
#                       "2 - solo game")
#                 res = True

