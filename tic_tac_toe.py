# board
# display board
# Play game
# handle turn
# check win -check rows, columns, diagonals
# check tie
# flip player

# -------Global Variables ---

# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won ? or tie?
winner = None

# Who's turn is  it
current_player = "X"


# ------------ Functions -------------

# Display board mapping keys to numeric pas as position
# Display board
def display_board():
    print(board[6] + '|' + board[7] + '|' + board[8])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[0] + '|' + board[1] + '|' + board[2])


# Player input
# handle turn
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    # Put the game piece on the board
    board[position] = player

    # Show the game board
    display_board()


# check the condition for game to over
# check if game over
def check_if_game_over():
    check_if_win()
    check_for_tie()

    return


# check if win
def check_rows():
    # set up global variable
    global game_still_going
    global winner

    # check if any row is having same values and is not empty
    row_1 = board[6] == board[7] == board[8] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[0] == board[1] == board[2] != '-'

    # if any row does have a match, flag that a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner X or O
    if row_1:
        print('row_1')
        winner = board[6]
        return print(winner + " won")
    elif row_2:
        print('row_2')
        winner = board[3]
        return print(winner + " won")
    elif row_3:
        print('row_3')
        winner = board[0]
        return print(winner + " won")
    return


def check_columns():
    # set up global variable
    global game_still_going
    global winner

    # check if any row is having same values and is not empty
    column_1 = board[6] == board[3] == board[0] != '-'
    column_2 = board[7] == board[4] == board[1] != '-'
    column_3 = board[8] == board[5] == board[2] != '-'

    # if any row does have a match, flag that a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner X or O
    if column_1:
        print('column_1')
        winner = board[6]
        return print(winner + " won")
    elif column_2:
        print('column_2')
        winner = board[7]
        return print(winner + " won")
    elif column_3:
        print('column_3')
        winner = board[8]
        return print(winner + " won")
    return


def check_diagonal():
    # set up global variable
    global game_still_going
    global winner

    # check if any row is having same values and is not empty
    diagonal_1 = board[6] == board[4] == board[2] != '-'
    diagonal_2 = board[8] == board[4] == board[0] != '-'

    # if any row does have a match, flag that a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner X or O
    if diagonal_1:
        print('diagonal_1')
        winner = board[2]
        return print(winner + " won")
    elif diagonal_2:
        print('diagonal_2')
        winner = board[0]
        return print(winner + " won")
    return


def check_if_win():
    global winner
    # check rows
    check_rows()
    # column
    check_columns()
    # diagonals
    check_diagonal()
    return


def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        print('Tie')
        return


def flip_player():
    # global variable
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


# -----------------Game Function-----------------
# Play game
def play_game():
    display_board()
    global game_still_going
    while game_still_going:
        # print the player turn
        print(f"{current_player} turn to play")

        # handle game to arbitrary player
        handle_turn(current_player)

        # check if game is ended
        check_if_game_over()

        # flip to the other player
        flip_player()


play_game()
