import tkinter as tk

class TicTacToe:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, width=10, height=5, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.player = "X"
        self.player = 'O'


    def on_button_click(self, i):
        if self.buttons[i]["text"] != " ":
            return 
        self.buttons[i]["text"] = self.player

        if self.check_win(self.player):
            self.root.title("Player " + self.player + " wins!")
            return
        elif self.check_draw():
            self.root.title("It's a draw!")
            return

        self.player = "O" if self.player == "X" else "X"

    def check_win(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i, j, k in win_conditions:
            if self.buttons[i]["text"] == player and self.buttons[j]["text"] == player and self.buttons[k]["text"] == player:
                return True
        return False

    def check_draw(self):
        for button in self.buttons:
            if button["text"] == " ":
                return False
        return True

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
