lines = list(map(int, open("input.txt").readlines()))

# Part 1
print(sum(1 for i in range(1, len(lines)) if lines[i] > lines[i - 1]))

# Part 2
print(sum(1 for i in range(1, len(lines) - 1) if sum(lines[i : i + 3]) > sum(lines[i - 1: i + 2])))
