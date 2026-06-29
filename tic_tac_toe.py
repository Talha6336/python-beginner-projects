from termcolor import colored
X = colored('X', 'red')
O = colored('O', 'green')

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(board):
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]}')
        print(line)


def check_winner(board):
    # Row
    for row in board:  # [X,X,X]
        if row[0] == row[1] == row[2] != ' ':
            return True
    # Column
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True
    # Diagnols
    if board[0][0] == board[1][1] == board[2][2] != ' ' or\
            board[2][0] == board[1][1] == board[0][2] != ' ':
        return True

    return False


def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def get_postion(prompt):
    while True:

        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print("Invalid input!")


def get_move(current_player):
    while True:

        print(f"Player {current_player}'s turn")
        row = get_postion('Enter row(0-2): ')
        col = get_postion('Enter column(0-2): ')
        if board[row][col] == " ":
            board[row][col] = current_player
            break

        print("This spot is already taken")


def main():
    print_board(board)

    current_player = X
    while True:
        get_move(current_player)

        print_board(board)
        if check_winner(board):
            print(f'Player {current_player} wins!')
            break

        if is_full(board):
            print("Board is Full")
            break

        current_player = O if current_player == X else X


if __name__ == "__main__":
    main()
