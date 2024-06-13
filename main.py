import random

choices = ["X", "O"]
Player1 = random.choice(choices)
choices.remove(Player1)
Player2 = choices[0]
print("Player 1 has been assigned =", Player1)
print("Player 2 has been assigned =", Player2)


rows, cols = 3, 3
arr = [[' ' for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True

    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    return False


def play_game():
    current_player = Player1
    while True:
        print_board(arr)
        cord1 = int(input(f"{current_player}, enter the row index (0-2): "))
        cord2 = int(input(f"{current_player}, enter the column index (0-2): "))
        
        
        if arr[cord1][cord2] != ' ':
            print("This position is already filled. Please choose a different position.")
            continue
        
        # Place the player's symbol on the board
        arr[cord1][cord2] = current_player
        
        
        if check_win(arr, current_player):
            print_board(arr)
            print(f"Player {current_player} wins!")
            break
        
     
        if all(all(cell != ' ' for cell in row) for row in arr):
            print_board(arr)
            print("The game is a draw!")
            break
        
        # Switch turns to the other player
        current_player = Player2 if current_player == Player1 else Player1


play_game()
