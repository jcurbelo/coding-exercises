def _move_rows_left(board):
    def trim_left_zeros(row, start):
        zero_count = 0
        j = start
        while j <= 3 and row[j] == 0:
            j += 1
            zero_count += 1

        if zero_count:
            zero_list = [0] * zero_count
            del row[start: start + zero_count]
            row += zero_list

    for r in board:
        i = 0
        while i < 3:
            # Trimming zeros
            if r[i] == 0:
                trim_left_zeros(r, i)
            if r[i + 1] == 0:
                trim_left_zeros(r, i + 1)

            # Compare with next element
            if r[i + 1] == r[i]:
                r[i] += r[i + 1]
                del r[i + 1]
                r.append(0)
            i += 1


def _move_rows_right(board):
    def trim_right_zeros(row, start):
        zero_count = 0
        j = start
        while j >= 0 and row[j] == 0:
            j -= 1
            zero_count += 1

        if zero_count:
            zero_list = [0] * zero_count
            del row[start - zero_count + 1: start + 1]
            row[:0] = zero_list

    for r in board:
        i = 3
        while i > 0:
            # Trimming zeros
            if r[i] == 0:
                trim_right_zeros(r, i)
            if r[i - 1] == 0:
                trim_right_zeros(r, i - 1)
            # Compare with next element
            if r[i - 1] == r[i]:
                r[i] += r[i - 1]
                del r[i - 1]
                r.insert(0, 0)
            i -= 1


def _traspose(board):
    t_board = [[None] * 4 for i in xrange(4)]
    for i in xrange(4):
        for j in xrange(4):
            t_board[i][j] = board[j][i]
    return t_board


def _print_board(board):
    for r in board:
        print ' '.join([str(i) for i in r])

# t1 = [[2, 0, 0, 2],
# [4, 16, 8, 2],
# [2, 64, 32, 4],
# [1024, 1024, 64, 0]]

# t2 = [[2, 2, 4, 8],
# [4, 0, 4, 4],
# [16, 16, 16, 16],
# [32, 16, 16, 32]]

# t3 = [[2, 2, 0, 0],
# [0, 2, 0, 2],
# [0, 0, 0, 2048],
# [4, 4, 8, 8]]


def main():
    board = []
    for i in xrange(4):
        row = [int(i) for i in raw_input().split(' ')]
        board.append(row)
    d = input()

    if d == 0:  # left
        _move_rows_left(board)
    elif d == 1:  # up
        board = _traspose(board)
        _move_rows_left(board)
        board = _traspose(board)
    elif d == 2:  # right
        _move_rows_right(board)
    else:  # down
        board = _traspose(board)
        _move_rows_right(board)
        board = _traspose(board)
    _print_board(board)


if __name__ == '__main__':
    main()
