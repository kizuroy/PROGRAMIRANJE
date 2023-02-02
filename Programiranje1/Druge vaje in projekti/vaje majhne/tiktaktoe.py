board = [" " for i in range(9)]

def print_board():
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2] + " ")
        if i < 2:
            print("---+---+---")

def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i, j, k in win_conditions:
        if board[i] == player and board[j] == player and board[k] == player:
            return True
    return False

def check_draw():
    return " " not in board

player = "X"

while True:
    print_board()
    print(f"Player {player}, choose a spot:")
    spot = int(input()) - 1
    if 0 <= spot < 9 and board[spot] == " ":
        board[spot] = player
    else:
        print("Invalid move, try again.")
        continue
    if check_win(player):
        print_board()
        print(f"Player {player} wins!")
        break
    elif check_draw():
        print_board()
        print("It's a draw!")
        break
    player = "O" if player == "X" else "X"
