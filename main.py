import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic Tac Toe")

# Game logic
def check_win(board, player):
    for i in range(3):
        if (board[i][0]["text"] == player and board[i][1]["text"] == player and board[i][2]["text"] == player) or \
           (board[0][i]["text"] == player and board[1][i]["text"] == player and board[2][i]["text"] == player):
            return True

    if (board[0][0]["text"] == player and board[1][1]["text"] == player and board[2][2]["text"] == player) or \
       (board[0][2]["text"] == player and board[1][1]["text"] == player and board[2][0]["text"] == player):
        return True

    return False

def check_draw(board):
    for row in board:
        for button in row:
            if button["text"] == " ":
                return False
    return True

# Initialize the board
buttons = [[None]*3 for _ in range(3)]
current_player = random.choice(["X", "O"])

# Function to handle button click
def on_click(row, col):
    global current_player
    
    if buttons[row][col]["text"] == " ":
        buttons[row][col]["text"] = current_player
        
        if check_win(buttons, current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_draw(buttons):
            messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the board
def reset_board():
    global current_player
    current_player = random.choice(["X", "O"])
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = " "

# Create buttons for each cell
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the main event loop
root.mainloop()
