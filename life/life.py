"""
This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
We assumme that cells at the edges of the board are dead.
"""

board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

def initialize(board, positions):
    for x, y in positions:
        board[x][y] = 1
    return board

def count_live_neighbors(pos, board):
    """Count live neighbors of a cell."""
    neighbors = find_neighbors(pos, board)
    return sum([board[x][y] for x,y in neighbors])

def find_neighbors(cell, board):
    """Return the coordinates of the neighboring cells.

    cell -- coordinates of the position of the cell on the board e.g. [0, 1]
    board -- n x n grid containing cells that are either dead (0) or alive (1) e.g. [[0, 0], [0, 1]]
    """
    x, y = cell
    neighbors = []
    x_max = x + 1 if x + 1 < len(board) else x
    x_min = x - 1 if x - 1 >= 0 else x
    y_max = y + 1 if y + 1 < len(board) else y
    y_min = y - 1 if y - 1 >= 0 else y

    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if i != x or j != y:  # DeMorgan's 1st Law: negating conjuctions
                neighbors.append([i, j])

    return neighbors

def evolve(board):
    births, deaths = [], []

    for x in range(len(board)):
        for y in range(len(board)):
            n = count_live_neighbors([x, y], board)

            if board[x][y] and (n == 2 or n == 3):
                continue
            elif not board[x][y] and n == 3:
                births.append([x, y])
            else:
                if board[x][y]:
                    deaths.append([x, y])

    for x, y in births:
        board[x][y] = 1

    for x, y in deaths:
        board[x][y] = 0

def next_gen(board):
    while True:
        yield board
        evolve(board)

def print_board(board):
    for row in board:
        print(' '.join([str(c) for c in row]))

def main():
    live_cells = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]
    initialize(board, live_cells)
    gen = next_gen(board)

    for _ in range(5):
        print('\n----------------\n')
        print_board(next(gen))


if __name__ == '__main__':
    main()
