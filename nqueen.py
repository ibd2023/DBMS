'''
We place one queen per row, moving row by row. 
At each row we try all columns, but only “safe” ones—i.e. columns not already occupied, 
and diagonals not under attack. We keep three sets to track occupied columns and the 
two diagonal directions (r-c and r+c). Whenever we place a queen we update those sets, 
recurse to the next row, and then backtrack (remove the queen) to try the next column.

'''
def solve_one_n_queens(n=8):
    cols, diag1, diag2 = set(), set(), set()
    placement = [0] * n

    def backtrack(r):
        # if all rows are filled, we’ve found one complete solution
        if r == n:
            return True

        for c in range(n):
            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue

            # place queen
            cols.add(c); diag1.add(r-c); diag2.add(r+c)
            placement[r] = c

            # recurse; if it returns True, bubble up the success
            if backtrack(r+1):
                return True

            # otherwise undo and try next column
            cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)

        return False  # no valid column in this row

    backtrack(0)
    return placement

def print_one_board(n=8):
    sol = solve_one_n_queens(n)
    print("valid 8×8 solution:\n")
    for r in range(n):
        print(' '.join('Q' if c == sol[r] else '.' for c in range(n)))

print_one_board(8)
