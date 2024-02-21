import random


playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field_size_limit = 3
evalible_steeps = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def make_field() -> None:
    print("_" * 4 * field_size_limit)
    for i in range(field_size_limit):
        print((" " * 3 + "|") * 3)
        print(
            "",
            playing_field[i * 3],
            "|",
            playing_field[1 + i * 3],
            "|",
            playing_field[2 + i * 3],
            "|",
        )
        print(("_" * 3 + "|") * 3)


def step(player_steep, step_number) -> bool:
    if (
        step_number > 9
        or step_number < 1
        or playing_field[step_number - 1] in ("X", "O")
    ):
        return False
    playing_field[step_number - 1] = player_steep
    return True


def check_win() -> bool:
    wins = False

    win_combinations = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for i in win_combinations:
        if playing_field[i[0]] == playing_field[i[1]] == playing_field[i[2]]:
            wins = playing_field[i[0]]
    return wins


def pc_step() -> int:
    pc_steeps = random.choice(evalible_steeps)
    return pc_steeps


def game_start() -> None:
    player_steep = "X"
    steep = 1
    make_field()

    while steep < 10 and (check_win() == False):

        if player_steep == "X":
            try:
                step_number = abs(
                    int(
                        input(f"Выберите поле для хода {player_steep} цифрой,Выход=0: ")
                    )
                )
            except ValueError:
                print("Вы ввели не цифру")
                continue
            if step_number == 0:
                print(f"Игра окончена")
                break

        else:
            step_number = pc_step()
            print(f"Ход компьютера: {step_number}")

        if step(player_steep, step_number):
            evalible_steeps.remove(step_number)

            if player_steep == "X":
                player_steep = "O"
            else:
                player_steep = "X"

            make_field()
            steep += 1

        else:
            print("Поле уже занято, выберите другое поле")

    if steep == 10 and check_win() == False:
        print("Game Over Ничья")
    elif check_win() != False:
        print("Игра окончена победил", check_win())


if __name__ == "__main__":
    game_start()
