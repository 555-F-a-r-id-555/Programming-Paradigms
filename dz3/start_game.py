from dz3.game_mode import get_user_choice, coop_game, solo_game

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
