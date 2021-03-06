# Создание поля для игры
field = [['-' for x in range(4)] for y in range(4)]
field[0][0] = ' '
field[1][0] = field[0][1] = 1
field[2][0] = field[0][2] = 2
field[3][0] = field[0][3] = 3


def print_field():
    """ Выводит поле на консоль """
    for line in field:
        for char in line:
            print(char, end='\t')
        print()


def winner(player_sign):
    if any([
        field[1][1] == field[1][2] == field[1][3] == player_sign,
        field[2][1] == field[2][2] == field[2][3] == player_sign,
        field[3][1] == field[3][2] == field[3][3] == player_sign,
        field[1][1] == field[2][1] == field[3][1] == player_sign,
        field[1][2] == field[2][2] == field[3][2] == player_sign,
        field[1][3] == field[2][3] == field[3][3] == player_sign,
        field[1][1] == field[2][2] == field[3][3] == player_sign,
        field[1][3] == field[2][2] == field[3][1] == player_sign,
    ]):
        return player_sign


def player_turn(player_sign):
    """ Ход одного из игроков """
    # Цикл для работы с исключениями
    while True:
        try:
            player = input(f'Введите слитно номер строки и столбца (от 1 до 3), куда нужно поставить {player_sign}: ')
            line_number = int(player[0])
            column_number = int(player[1])

            if 1 <= line_number <= 3 and 1 <= column_number <= 3:
                if field[line_number][column_number] == '-':
                    field[line_number][column_number] = player_sign
                    break
                else:
                    print('Это поле уже занято, попробуйте еще раз')
            else:
                print('Неправильный диапазон - нужно вводить числа от 1 до 3')
        except ValueError:
            print('Нужно ввести 2 числа от 1 до 3!')
        except IndexError:
            print('Одного числа мало!')

    print_field()


print_field()
count = 0
# Основной цикл выполнения программы
while True:
    # Ход первого игрока
    player_turn('x')

    if winner('x') == 'x':
        print('Победил первый игрок!')
        break

    count += 1

    if count >= 9:
        print('Ничья!')
        break

    # Ход второго игрока
    player_turn('o')

    if winner('o') == 'o':
        print('Победил второй игрок!')
        break

    count += 1

