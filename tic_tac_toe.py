import random

players = [input('Введите имя первого игрока: '), input('Введите имя второго игрока: ')]

first_player = random.randrange(0, 2)
current_palyer = first_player
number_current_player = 0
game_field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
game_end = False

print(f'Крестики нолики - {players[0]} против {players[1]}')
print(f'Первым ходит игрок - { players[first_player]}')


def show_game_field_borders(n_row, n_col):
    if n_col == 0 and n_row == 0:
        print(' ', '1', ' 2', ' 3')
        print('1', end='')
        return ' '
    elif n_col == 0:
        return str(n_row + 1) + ' '
    else:
        return ''


def show_game_field():
    for id_row, row in enumerate(game_field):
        for id_col, col in enumerate(row):
            print(show_game_field_borders(id_row, id_col), end='')
            print(col, ' ', end='')

        print('\r')


def cell_input():
    global current_palyer
    current_palyer = first_player - current_palyer
    cell = list(map(int, input('Введите номер строки и колонки (через пробел): ').split()))
    game_field[cell[0] - 1][cell[1] - 1] = 'X'

    show_game_field()


show_game_field()


while not game_end:
    cell_input()


# game_field[0][2] = '1'