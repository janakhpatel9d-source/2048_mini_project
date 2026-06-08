import tkinter as tk
from tkinter import messagebox

from main import (
    add_new_tile,
    create_board,
    move_left,
    move_right,
    move_up,
    move_down,
    check_win,
    game_over
)
root = tk.Tk()

root.title("2048 Game")
root.geometry("550x700")

root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="2048",
    font=("Helvetica", 32, "bold"),
    fg="#f9f6f2",
    bg="#1e1e1e"
)
title.pack(pady=10)
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Helvetica", 16, "bold"),
    bg="#333333",
    fg="white",
    padx=15,
    pady=8
)
score_label.pack(pady=10)


grid_frame = tk.Frame(root, bg="#1e1e1e")
grid_frame.pack()

cells = []

for i in range(4):
    row = []

    for j in range(4):
        cell = tk.Label(
            grid_frame,
            text="",
            width=6,
            height=3,
            font=("Helvetica", 24, "bold"),
           relief="flat",
            borderwidth=0
        )

        cell.grid(row=i, column=j, padx=5, pady=5)

        row.append(cell)

    cells.append(row)

board = create_board()
add_new_tile(board)
add_new_tile(board)
score = 0
game_won = False
game_finished = False

def update_grid():

    colors = {
    0: "#2d2d2d",
    2: "#e0e0e0",
    4: "#d6d6d6",
    8: "#ff9800",
    16: "#ff7043",
    32: "#f4511e",
    64: "#e53935",
    128: "#ffca28",
    256: "#ffc107",
    512: "#ffb300",
    1024: "#ffa000",
    2048: "#ffd54f"
}
    print(board)
    for i in range(4):
        for j in range(4):

            value = board[i][j]

            if value == 0:
                cells[i][j].config(
                    text="",
                    bg=colors[0],
                    fg="white"
                    )
            else:
                if value in [2, 4]:
                    text_color = "#776e65"
                else:
                    text_color = "white"

                cells[i][j].config(
                    text=str(value),
                    bg=colors.get(value, "#3c3a32"),
                    fg=text_color
                    )
def restart_game():
    global board, score, game_won, game_finished

    board = create_board()

    add_new_tile(board)
    add_new_tile(board)

    score = 0
    game_won = False
    game_finished = False

    score_label.config(text="Score: 0")

    update_grid()
restart_button = tk.Button(
    root,
    text="🎮 New Game",
    font=("Helvetica", 12, "bold"),
    bg="#444444",
    fg="white",
    activebackground="#666666",
    activeforeground="white",
    padx=12,
    pady=6,
    command=restart_game
)

restart_button.pack(pady=5)


def key_press(event):
    global board, score, game_won, game_finished

    key = event.keysym.lower()

    gained = 0
    old_board = [row[:] for row in board]

    if key == "a":
        board, gained = move_left(board)

    elif key == "d":
        board, gained = move_right(board)

    elif key == "w":
        board, gained = move_up(board)

    elif key == "s":
        board, gained = move_down(board)

    else:
        return

    score += gained

    if board != old_board:
        add_new_tile(board)

    score_label.config(text=f"Score: {score}")

    update_grid()

    if check_win(board) and not game_won:
        game_won = True

        messagebox.showinfo(
            "Congratulations!",
            f"You reached 2048!\n\nScore: {score}"
        )

    if game_over(board) and not game_finished:
        game_finished = True

        messagebox.showerror(
            "Game Over",
            f"No more moves available!\n\nFinal Score: {score}"
        )
update_grid()
  
root.bind("<Key>", key_press)

root.mainloop()