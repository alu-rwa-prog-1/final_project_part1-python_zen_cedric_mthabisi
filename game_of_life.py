from life import life

def main():
    # TODO ask user for the type of spaceship they want to see playing
    # Play with the appropriate ship -> here dummy HeavyWeight 
    board = life.HeavyWeightShip(20, 20)
    activate_cells(board, board.live_cells)
    gen = next_gen(board)

    # TODO ask for the number of generation for Life

    for _ in range(5):
        print('\n----------------\n')
        print(next(gen))


if __name__ == '__main__':
    main()