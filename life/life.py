"""
    This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
    We assumme that cells at the edges of the board are dead.
"""
import boards

def next_gen(board):
    """Yield the next generation of the Game of Life board."""
    while True:
        board.update()
        yield board

def run():
    """Reads command-line arguments and starts a game with those options."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Conway's Game of Life")
    parser.add_argument('-b', type=str, metavar='BOARD', help='selects the game board',
                        choices=[
                            'glider',
                            'lightweight-ship',
                            'middlewight-ship',
                            'heavyweight-ship',
                        ])
    parser.add_argument('--size', type=int,
                        help='selects board size (number of columns and rows)', default=10)
    args = parser.parse_args()

    size = args.size
    board = boards.Board(size, size)

    if args.b == 'glider':
        board = boards.Glider(size, size)
    elif args.b == 'lightweight-ship':
        board = boards.LightWeightShip(size, size)
    elif args.b == 'middleweight-ship':
        board = boards.MiddleWeightShip(size, size)
    elif args.b == 'heavyweight-ship':
        board = boards.HeavyWeightShip(size, size)

    user_action = ''
    new_gen = next_gen(board)
    print(board)

    while user_action != 'q':
        user_action = input('Press Enter to see new generation or Q + Enter to quit: ')
        if user_action == '':
            print(next(new_gen))


if __name__ == '__main__':
    run()
