from dz3.check_win import check_state
from dz3.constant import *
from dz3.human_and_ai_turn import human_turn, ai_turn
from dz3.print_field import initialize, print_field


def coop_game():
    while True:
        field = initialize()
        print_field()
        while True:
            print("Ход первого игрока")
            human_turn(field, DOT_HUMAN_X)
            print_field()
            if check_state(field, DOT_HUMAN_X, "Игрок 'X' победил!"):
                break
            print("Ход второго игрока")
            human_turn(field, DOT_HUMAN_O)
            print_field()
            if check_state(field, DOT_HUMAN_O, "Игрок '0' победил!"):
                break
        if not play_again():
            break


def solo_game():
    while True:
        try:
            version_ai = int(input("Введите уровень сложности (1 - случайный ход, 2 - умный AI): "))
            if version_ai not in [1, 2]:
                print("Ошибка! Пожалуйста, выберите 1 или 2.")
                continue
        except ValueError:
            print("Ошибка! Введите число.")
            continue

        field = initialize()
        print_field()
        while True:
            human_turn(field, DOT_HUMAN_X)
            print_field()
            if check_state(field, DOT_HUMAN_X, "Вы победили!"):
                break
            ai_turn(field, version_ai)
            print_field()
            if check_state(field, DOT_AI, "Победил компьютер!"):
                break
        if not play_again():
            break


def play_again():
    return input("Желаете сыграть еще раз? (Y - да): ").strip().lower() == "y"


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
