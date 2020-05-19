'''Created By Khemchand'''

import random

print('Welcome to Tic Tac Toe!')

# check that entered position have empty space or not
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

# player choose there position
def player_choice(board):
    position = int(input('Enter your position(number 1-9) '))
    if space_check and position <= 9:
        return position
    else:
        return False

# reply the game on the basis of player input
def replay():
    while True:
        choice = input("Are you want to play again(y/n) ")
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            continue


# tic tac toe board 
def display_board(board):
    print('\n'*100) # make the screen empty
    dict1 = {1: '   |   |   ', 3: '---|---|---'}
    # list1 = [1,2,1,3,1,2,1,3,1,2,1]
    board1 = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    j = i = 1
    while i < len(board1) and j < len(board):
        board1[i] = board[j]
        i += 1
        j += 1

    print(dict1[1])
    print(' ' + board1[7] + ' ' + '|' + ' ' + board1[8] + ' ' + '|' + ' ' + board1[9] + ' ')
    print(dict1[1])
    print(dict1[3])

    print(dict1[1])
    print(' ' + board1[4] + ' ' + '|' + ' ' + board1[5] + ' ' + '|' + ' ' + board1[6] + ' ')
    print(dict1[1])
    print(dict1[3])

    print(dict1[1])
    print(' ' + board1[1] + ' ' + '|' + ' ' + board1[2] + ' ' + '|' + ' ' + board1[3] + ' ')
    print(dict1[1])

# player choose there mark
def player_input():
    while True:
        player_1 = input("Player 1 choose your mark, 'X'or 'O' ")
        if player_1.lower() == 'x':
            player_1 = player_1.upper()
            player_2 = 'O'
            break
        elif player_1.lower() == 'o':
            player_1 = player_1.upper()
            player_2 = 'X'
            break
        else:
            pass
    list1 = [player_1, player_2]
    return list1

# place the marker on board at given position which is entered by user
def place_marker(board, marker, position):
        
    board[position] = marker
    return board

# select the winner
def win_check(board, mark):
    if board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    elif board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    else:
        return False

# choose that which player place their marker first
def choose_first():
    if random.randint(1, 2) == 1:
        return 'player_1'
    else:
        return 'player_2'


# check that board is full or not
def full_board_check(board):
    for i in board:
        if i == ' ':
            return False

    return True


while True:
    t = player_input()
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # contain the marks on board
    position = 1 
    c = choose_first()
    while True:

        if c == 'player_1':

            display_board(board)
            print('Player 1 turn')
            position = player_choice(board)
            if position == False:
                print("Wrong Input! Try Again")
                continue
            if space_check(board, position):
                place_marker(board, t[0], position)
            else:
                print("Place is already marked!!")

            if win_check(board, t[0]):
                display_board(board)
                print("Congratulations! Player 1 wins the game")
                break
            if full_board_check(board):
                display_board(board)
                print('No one wins the game play again')
                break

            display_board(board)
            print('Player 2 turn')
            position = player_choice(board)
            if space_check(board, position):
                place_marker(board, t[1], position)
            else:
                print("Place is already marked!!")
            if win_check(board, t[1]):
                display_board(board)
                print("Congratulations! Player 2 wins the game")
                break
            if full_board_check(board):
                display_board(board)
                print('No one wins the game play again')
                break

        elif c == 'player_2':

            display_board(board)
            print('Player 2 turn')
            position = player_choice(board)
            if space_check(board, position):
                place_marker(board, t[1], position)
            else:
                print("Place is already marked!!")
            if win_check(board, t[1]):
                display_board(board)
                print("Congratulations! Player 2 wins the game")
                break
            if full_board_check(board):
                display_board(board)
                print('No one wins the game play again')
                break

            display_board(board)
            print('Player 1 turn')
            position = player_choice(board)
            if space_check(board, position):
                place_marker(board, t[0], position)
            else:
                print("Place is already marked!!")
            if win_check(board, t[0]):
                display_board(board)
                print("Congratulations! Player 1 wins the game")
                break
            if full_board_check(board):
                display_board(board)
                print('No one wins the game play again')
                break

    if not replay():
        break
