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


print_field()

while True:
    # Ход первого игрока
    player1 = input('Введите слитно номер строки и столбца (от 1 до 3), куда нужно поставить крестик: ')
    line_number = int(player1[0])
    column_number = int(player1[1])

    while True:
        if 1 <= line_number <= 3 and 1 <= column_number <= 3:
            if field[line_number][column_number] == '-':
                field[line_number][column_number] = 'x'
                break
            else:
                player1 = input('Это поле уже занято, попробуйте еще раз: ')
                line_number = int(player1[0])
                column_number = int(player1[1])
        else:
            player1 = input('Нужно вводить числа от 1 до 3, попробуйте еще раз: ')
            line_number = int(player1[0])
            column_number = int(player1[1])
    print_field()

    if winner('x') == 'x':
        print('Победил первый игрок!')
        break

    # Ход второго игрока
    player2 = input('Введите слитно номер строки и столбца (от 1 до 3), куда нужно поставить нолик: ')
    line_number = int(player2[0])
    column_number = int(player2[1])

    while True:
        if 1 <= line_number <= 3 and 1 <= column_number <= 3:
            if field[line_number][column_number] == '-':
                field[line_number][column_number] = 'o'
                break
            else:
                player2 = input('Это поле уже занято, попробуйте еще раз: ')
                line_number = int(player2[0])
                column_number = int(player2[1])
        else:
            player2 = input('Нужно вводить числа от 1 до 3, попробуйте еще раз: ')
            line_number = int(player2[0])
            column_number = int(player2[1])
    print_field()

    if winner('o') == 'o':
        print('Победил второй игрок!')
        break
