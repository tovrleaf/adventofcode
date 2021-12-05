lines = list(map(str.strip, open("input.txt").readlines()))

numbers = list(map(int, lines.pop(0).split(",")))

def get_matcher():
    return [[False] * 5 for _ in range(5)]

boards, matches = [], []

b = []
for x in lines[1:]:
    if x != "":
        b.append(list(map(int, x.split())))
        continue
    boards.append(b)
    matches.append(get_matcher())
    b = []

def check_number(number, board, matches):
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == number:
                matches[i][j] = True
                return True
    return False

def check_board(matches):
    return any(all(r) for r in matches) or any(all(c) for c in zip(*matches))

def check(numbers, boards, matches):
    solved = []
    for n in numbers:
        for b in range(len(boards)):
            if b in solved:
                continue
            if check_number(n, boards[b], matches[b]):
                if check_board(matches[b]):
                    solved.append(b)
                    yield (n, b)

def summarize_board(board, matches):
    total = 0
    for i in range(len(board)):
        total += sum([x[0] for x in filter(lambda x: x[1] is False, list(zip(board[i], matches[i])))])

    return total

ret = check(numbers, boards, matches)
n, b = next(ret)
score = summarize_board(boards[b], matches[b])

# Part 1
print(score * n)

# Part 2
*_, (n, b) = ret
score = summarize_board(boards[b], matches[b])
print(score * n)
