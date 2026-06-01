import random

SIZE = 4

def create_board():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    return board

def add_new_tile(board):
    empty_cells = []

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                empty_cells.append((i, j))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2
def print_board(board):
    print("\n" + "-" * 25)

    for row in board:
        for cell in row:
            print(f"{cell:4}", end="")
        print()

    print("-" * 25)

def compress(row):
    new_row = [num for num in row if num != 0]

    while len(new_row) < SIZE:
        new_row.append(0)

    return new_row

board = create_board()

add_new_tile(board)
add_new_tile(board)

for row in board:
    print(row)



def merge(row):
    for i in range(SIZE - 1):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0

    return row



def move_left(board):
    new_board = []

    for row in board:
        row = compress(row)
        row = merge(row)
        row = compress(row)

        new_board.append(row)

    return new_board



def move_right(board):
    new_board = []

    for row in board:
        row.reverse()          # Reverse row
        row = compress(row)
        row = merge(row)
        row = compress(row)
        row.reverse()          # Reverse back

        new_board.append(row)

    return new_board



def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)

    return board


def move_down(board):
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)

    return board

def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def game_over(board):

    # Any empty cell?
    for row in board:
        if 0 in row:
            return False

    # Check horizontal merges
    for i in range(SIZE):
        for j in range(SIZE - 1):
            if board[i][j] == board[i][j + 1]:
                return False

    # Check vertical merges
    for j in range(SIZE):
        for i in range(SIZE - 1):
            if board[i][j] == board[i + 1][j]:
                return False

    return True

if __name__ == "__main__":

    board = create_board()

    add_new_tile(board)
    add_new_tile(board)

    while True:

        print_board(board)

        move = input("Enter move (W/A/S/D) or Q to quit: ").lower()

        if move == "q":
            print("Game Over!")
            break

        old_board = [row[:] for row in board]

        if move == "a":
            board = move_left(board)

        elif move == "d":
            board = move_right(board)

        elif move == "w":
            board = move_up(board)

        elif move == "s":
            board = move_down(board)

        else:
            print("Invalid move!")
            continue

        if board != old_board:
            add_new_tile(board)

        # Win Check
        if check_win(board):
            print_board(board)
            print("🎉 You reached 2048! You Win!")
            break
        if game_over(board):
            print_board(board)
            print("💀 Game Over!")
            break