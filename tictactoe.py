import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики-Нолики")
        self.root.resizable(False, False)

        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def on_button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Гра завершена", f"Гравець {self.current_player} переміг!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Гра завершена", "Нічия!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальні лінії
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальні лінії
            [0, 4, 8], [2, 4, 6]              # діагональні лінії
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
