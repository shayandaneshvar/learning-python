# Functions
def print_board(x):
    print("----------------")
    for i in range(0, 3):
        print(x[i])
    print("----------------")


def get_winner(turn, board):
    if (board[0][0] == board[0][1] == board[0][1] != '0') or \
            (board[1][0] == board[1][1] == board[1][1] != '0') or \
            (board[2][0] == board[2][1] == board[2][1] != '0') or \
            (board[0][0] == board[1][0] == board[2][0] != '0') or \
            (board[0][1] == board[1][1] == board[2][1] != '0') or \
            (board[0][2] == board[1][2] == board[2][2] != '0') or \
            (board[0][0] == board[1][1] == board[2][2] != '0') or \
            (board[2][0] == board[1][1] == board[0][2] != '0'):
        return (turn - 1) % 2 + 1
    else:
        return 0


def start_game():
    board = [['0', '0', '0'],
             ['0', '0', '0'],
             ['0', '0', '0']]
    turn = 0
    while True:
        print_board(board)
        x_axis = input("Enter X:")
        y_axis = input("Enter Y:")
        if (not (0 < int(y_axis) < 4)) or not (0 < int(x_axis) < 4):
            print("Enter Correct Input 0 < x, y < 4")
            continue
        char = ''
        if turn % 2 == 0:
            char = 'X'
        else:
            char = 'Y'
        if board[int(y_axis) - 1][int(x_axis) - 1] == '0':
            board[int(y_axis) - 1][int(x_axis) - 1] = char
            turn += 1
        char = get_winner(turn, board)
        if char != 0:
            print(int(char))
            print("player " + str(char) + " has Won!")
            break
    print("The Game Has Ended!")


# Starting the Program
print("=======================")
print("☻ Welcome to The XO ☻")
print("=======================")
start_game()
b = input("Do you want to play Again?(y,n)")
while True:
    if b == 'y':
        start_game()
    else:
        print("Exiting!")
        break
