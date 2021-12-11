data = [list(line) for line in map(str.strip, open("input.txt").readlines())]

brackets =  {"(": ")", "[": "]", "{": "}", "<": ">"}
invalid = dict.fromkeys(brackets.values(), 0)

mismatch_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
corrupted = {}

def syntax_error(ind, line):
    expect = []
    wrong = []
    for br in line:
        if br in brackets:
            expect.append(brackets[br])
            continue

        if br != expect.pop():
            invalid[br] += 1
            return

    score = 0
    for c in reversed(expect):
        score = score * 5 + ' )]}>'.index(c)

    corrupted[ind] = score

for i, line in enumerate(data):
    syntax_error(i, line)


# Part 1
print(sum(v * mismatch_score[k] for k, v in invalid.items()))
# Part 2
print(sorted(corrupted.values())[len(corrupted)//2])
