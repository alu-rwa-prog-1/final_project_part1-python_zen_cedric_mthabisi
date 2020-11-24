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

def initialize(board_, positions):
    for x, y in positions:
        board_[x][y] = 1
    return board_

def count_live_neighbors(pos, board_):
    """Count live neighbors of a cell."""
    x, y = pos
    neighbors = []
    board_height = len(board_)

    if x == 0 and y == 0:
        neighbors += [board_[x][y + 1], board_[x + 1][y], board_[x + 1][y + 1]]
    elif x == board_height - 1 and y == board_height - 1:
        neighbors += [board_[x][y - 1], board_[x - 1][y - 1], board_[x - 1][y]]
    elif x == 0 and y == board_height - 1:
        neighbors += [board_[x][y - 1], board_[x + 1][y - 1], board_[x + 1][y]]
    elif x == board_height - 1 and y == 0:
        neighbors += [board_[x][y + 1], board_[x - 1][y], board_[x - 1][y + 1]]
    elif x == 0:
        neighbors += [board_[x][y - 1], board_[x][y + 1]] + board_[x + 1][y - 1: y + 2]
    elif x == board_height - 1:
        neighbors += [board_[x][y - 1], board_[x][y + 1]] + board_[x - 1][y - 1: y + 2]
    elif y == 0:
        neighbors += [board_[x + 1][y], board_[x - 1][y],
                      board_[x - 1][y + 1], board_[x][y + 1], board_[x + 1][y + 1]]
    elif y == board_height - 1:
        neighbors += [board_[x + 1][y], board_[x - 1][y],
                      board_[x - 1][y - 1], board_[x][y - 1], board_[x + 1][y - 1]]
    else:
        neighbors += board_[x - 1][y - 1: y + 2] + [board_[x][y - 1], board_[x][y + 1]] + board_[x + 1][y - 1: y + 2]

    return sum(neighbors)

def evolve(board_):
    births, deaths = [], []

    for x in range(len(board_)):
        for y in range(len(board_)):
            n = count_live_neighbors([x, y], board_)

            if board_[x][y] and (n == 2 or n == 3):
                continue
            elif not board_[x][y] and n == 3:
                births.append([x, y])
            else:
                if board_[x][y]:
                    deaths.append([x, y])

    for x, y in births:
        board_[x][y] = 1

    for x, y in deaths:
        board_[x][y] = 0

def next_gen(board_):
    while True:
        yield board_
        evolve(board_)

def print_board(board_):
    for row in board_:
        print(' '.join([str(c) for c in row]))

def main():
    live_cells = [[2, 2], [2, 3], [3, 2], [3, 3], [4, 4], [4, 5], [5, 4], [5, 5]]
    initialize(board, live_cells)
    gen = next_gen(board)

    for _ in range(5):
        print_board(next(gen))


if __name__ == '__main__':
    main()
