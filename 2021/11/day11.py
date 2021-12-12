def get_data():
    return [[int(value) for value in line.strip()] for line in open("input.txt").readlines()]

def get_adjanced(col, row):
    ret = []
    for w in [-1, 0, 1]:
        for h in [-1, 0, 1]:
            if w == 0 and h == 0:
                continue
            x, y = row + w, col + h
            if 0 <= x < 10 and 0 <= y < 10:
                ret.append((x, y))
    return ret


def flash(board, stack, row, col):
    board[row][col] = 0
    stack.append((row, col))
    return 1

def handle(board):
    flashes, stack = 0, []
    for r in range(10):
        for c in range(10):
            board[r][c] += 1
            if board[r][c] > 9:
                flashes += flash(board, stack, r, c)
    while stack:
        r, c = stack.pop()
        for r1, c1 in get_adjanced(c, r):
            # not reset this round
            if board[r1][c1] > 0:
                board[r1][c1] += 1
                if board[r1][c1] > 9:
                    flashes += flash(board, stack, r1, c1)
    return flashes


# Part 1
data1 = get_data()
print(sum(handle(data1) for _ in range(100)))


# Part 2
times = 0
data2 = get_data()
while handle(data2) != 100:
    times += 1
times += 1
print(times)
