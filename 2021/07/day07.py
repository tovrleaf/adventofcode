subs = list(map(int, open("input.txt").readline().split(",")))

# Part 1
print(min([sum(abs(pos - crab) for crab in subs) for pos in range(len(subs))]))
# Part 2
print(min([sum(sum(range(abs(pos - crab) + 1)) for crab in subs) for pos in range(len(subs))]))
