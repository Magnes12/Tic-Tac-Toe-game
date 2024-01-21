import os

clear = lambda: os.system('cls')


def display_board(board):

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----+-----+-----")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----+-----+-----")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


board = [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ']


def player_x():

    player_x = int(input("Which field? (X) "))
    if board[player_x] != " O ":
        board[player_x] = " X "
    else:
        print("This field seems taken")
        player_x_2 = int(input("Choose another field? (X) "))
        board[player_x_2] = " X "


def player_o():

    player_o = int(input("Which field? (O) "))
    if board[player_o] != " X ":
        board[player_o] = " O "
    else:
        print("This field seems taken")
        player_o_2 = int(input("Choose another field? (O) "))
        board[player_o_2] = " O "

    clear()


def check_if_win(board):
    win_comb = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
        ]
    for com in win_comb:
        if all(board[pos] == " X " for pos in com):
            return True
        elif all(board[pos] == " O " for pos in com):
            return True
    return False


game_is_on = True

while game_is_on:
    display_board(board)
    player_x()
    if check_if_win(board):
        display_board(board)
        print("Player X wins!")
        break
    display_board(board)
    player_o()
    if check_if_win(board):
        display_board(board)
        print("Player X wins!")
        break
