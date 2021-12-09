data = [[int(value) for value in line.strip()] for line in open("input.txt").readlines()]

def get_adjanced(data, col, row):
    ret = []
    for w, h in (-1, 0), (1, 0), (0, -1), (0, 1):
        x, y = row + w, col + h
        if 0 <= x < len(data[0]) and 0 <= y < len(data):
            ret.append((x, y))
    return ret

def get_basil(data, x, y):
    visited = [(x, y)]
    area = [(x, y)]
    while area:
        adj_col, adj_row = area.pop(0)
        for i1, j1 in get_adjanced(data, adj_row, adj_col):
            if (i1, j1) not in visited and data[i1][j1] != 9:
                visited.append((i1, j1))
                area.append((i1, j1))

    return len(visited)

risk = 0
basins = []
for x, row in enumerate(data):
    for y, col in enumerate(row):
        adj = get_adjanced(data, x, y)
        if all(data[y1][x1] > data[x][y] for x1, y1 in adj):
            risk += col + 1
            basins.append(get_basil(data, x, y))


# Part 1
print(risk)
i = 1
for x in sorted(basins)[-3:]:
    i *= x
print(i)
