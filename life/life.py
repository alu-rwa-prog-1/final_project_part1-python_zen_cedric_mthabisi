""" 
    Author: Mthabisi Ndlovu, Cedric Murairi
    
    This program implements the Game of Life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
    We assumme that cells at the edges of the board are dead.
"""
import boards

def next_gen(board):
    """Yield the next generation of the Game of Life board."""
    while True:
        board.update()
        yield board

def write_to_file(username, board_type, board_size):
    """write to file the user actions with the game board"""
    new_file = open(f'life/user_sessions/{username}.txt', 'a')

    new_file.write('\n-----------------------------\n')
    new_file.write(f'Username: {username} \n')
    new_file.write(f'Board type: {board_type} \n')
    new_file.write(f'Board size: {board_size} \n')
    new_file.close()

def run():
    """Reads command-line arguments and starts a game with those options."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Conway's Game of Life")
    parser.add_argument('-b', type=str, metavar='BOARD', help='selects the game board',
                        choices=[
                            'glider',
                            'lightweight-ship',
                            'middleweight-ship',
                            'heavyweight-ship',
                        ])
    parser.add_argument('--size', type=int,
                        help='selects board size (number of columns and rows)', default=10)
    parser.add_argument('--username', help='selects username')
    args = parser.parse_args()

    size = args.size
    board = boards.Board(size, size)

    username = args.username

    write_to_file(username, args.b, size)

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
