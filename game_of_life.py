"""
    This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
    We assumme that cells at the edges of the board are dead.
"""

from life import boards as br

def main():
    board = br.HeavyWeightShip(15, 15)
    br.activate_cells(board, board.live_cells)
    gen = br.next_gen(board)

    for _ in range(5):
        print('\n----------------\n')
        print(next(gen))


if __name__ == '__main__':
    main()