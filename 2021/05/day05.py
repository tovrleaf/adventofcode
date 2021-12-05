lines = list(map(str.strip, open("input.txt").readlines()))

area1 = {}
area2 = {}

def mark(area, x, y):
    if x not in area:
        area[x] = {}
    if y not in area[x]:
        area[x][y] = 0
    area[x][y] += 1
    return area

def mark_width(area, x, y, width):
    for i in range(width):
        area = mark(area, x + i, y)
    return area

def mark_height(area, x, y, height):
    for i in range(height):
        area = mark(area, x, y + i)
    return area

def mark_diagonal(area, x1, y1, x2, y2):
    step_x = -1 if x2 < x1 else 1
    step_y = -1 if y2 < y1 else 1

    y = y1
    for x in range(x1, x2 + step_x, step_x):
        area = mark(area, x, y)
        y += step_y
    return area

def mark_orthogonal(area, x1, y1, x2, y2):
    if x1 == x2:
        return mark_height(area, x1, min(y1, y2), abs(y1 - y2) + 1)
    return mark_width(area, min(x1, x2), y1, abs(x1 - x2) + 1)


for l in lines:
    (x1, y1), (x2, y2) = list(map(lambda x: map(int, x.split(',')), l.split(' -> ')))
    is_straight = (x1 == x2 or y1 == y2)
    is_diagonal = (abs(x1 - x2) == abs(y1 - y2))
    # Part 1
    if is_straight:
        area1 = mark_orthogonal(area1, x1, y1, x2, y2)
    # Part 2
    if  is_straight or is_diagonal:
        area2 = mark_orthogonal(area2, x1, y1, x2, y2) if is_straight else mark_diagonal(area2, x1, y1, x2, y2)

# Part 1
r = sum(1 for x in area1.keys() for y in area1[x].keys() if area1[x][y] > 1)
print(r)

# Part 2
r = sum(1 for x in area2.keys() for y in area2[x].keys() if area2[x][y] > 1)
print(r)
