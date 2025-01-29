from dz3.constant import *

""" Проверяет, есть ли на поле свободные клетки. """
def check_draw(field):
    return not any(DOT_EMPTY in row for row in field)


""" Проверяет, может ли игрок с заданной фишкой выиграть за `steps_ahead` ходов. """
def check_win(field, dot, steps_ahead=0):
    win_length = FIELD_SIZE - steps_ahead  # Количество фишек, необходимых для победы
    return check_win_diagonal(field, dot, win_length) or check_win_horizontal_vertical(field,dot, win_length)

""" Проверяет победу по двум диагоналям. """
def check_win_diagonal(field, dot, win_length):
    for start in range(FIELD_SIZE - win_length + 1):
        if all(field[start + i][start + i] == dot for i in range(win_length)):
            return True
        if all(field[start + i][FIELD_SIZE - 1 - (start + i)] == dot for i in range(win_length)):
            return True
    return False

""" Проверяет победу по горизонтали и вертикали. """
def check_win_horizontal_vertical(field, dot, win_length):
    for i in range(FIELD_SIZE):
        for start in range(FIELD_SIZE - win_length + 1):
            if all(field[i][start + j] == dot for j in range(win_length)):
                return True
            if all(field[start + j][i] == dot for j in range(win_length)):
                return True
    return False


""" Проверяет текущее состояние игры (победа, ничья или продолжаем). """
def check_state(field, dot, win_message, steps_ahead=0):
    if check_win(field,dot, steps_ahead):
        print(win_message)
        return True
    if check_draw(field):
        print("Ничья!")
        return True
    return False  # Игра продолжается
