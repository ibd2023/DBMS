def print_board(b):
    """Display the current board."""
    for row in b:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(b, mark):
    """Return True if mark ('X' or 'O') has three in a row."""
    # rows, columns, diagonals
    win_states = [
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]],
    ]
    return [mark]*3 in win_states

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    current, other = 'X', 'O'
    moves = 0

    while True:
        print_board(board)
        # get a valid move
        try:
            r, c = map(int, input(f"Player {current}, enter row,col (0–2): ").split(','))
            if board[r][c] != ' ':
                print("Cell occupied—try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input—use format row,col with 0 ≤ row,c ≤ 2.")
            continue

        board[r][c] = current
        moves += 1

        if check_winner(board, current):
            print_board(board)
            print(f"🎉 Player {current} wins!")
            break
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # swap players
        current, other = other, current

if __name__ == '__main__':
    tic_tac_toe()
