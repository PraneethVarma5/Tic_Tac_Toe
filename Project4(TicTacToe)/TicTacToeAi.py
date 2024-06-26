import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.is_single_player = True  # Flag to determine if it's a single-player game

        # Create buttons for the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Helvetica", 24), height=2, width=5,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Create a label to display the current player
        self.player_label = tk.Label(self.window, text=f"Current Player: {self.current_player}")
        self.player_label.grid(row=3, columnspan=3)

    def make_move(self, position):
        if self.board[position] == "":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_label.config(text=f"Current Player: {self.current_player}")
                if self.is_single_player and self.current_player == "O":
                    self.make_computer_move()

    def make_computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ""]
        if empty_cells:
            random_position = random.choice(empty_cells)
            self.make_move(random_position)

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return self.board[combo[0]]
        return None

    def reset_board(self):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].config(text="")
        self.current_player = "X"
        self.player_label.config(text=f"Current Player: {self.current_player}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

