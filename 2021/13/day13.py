dots, folds = open("input.txt").read().split("\n\n")
dots = [map(int, x.split(",")) for x in dots.split("\n")]

_ = [x.strip().split()[2].split("=") for x in folds.split("\n") if x != ""]
folds = []
for axis, loc in _:
    folds.append((axis, int(loc)))

def new_coord(axis, fold_size, x, y):
    if axis == 'x':
        return (x if x < fold_size else 2 * fold_size - x, y)
    return (x, y if y < fold_size  else 2 * fold_size - y)

def fold(dots, folds):
    for axis, number in folds:
        new_coords = set()
        for x, y in dots:
            new_coords.add(new_coord(axis, number, x, y))
        dots = new_coords
    return dots

dots = fold(dots, folds[:1])
# Part 1
assert 795 == len(dots)

def grid(dots):
    mx = max(x for x, _ in dots) + 1
    my = max(y for _, y in dots) + 1
    for y in range(my):
        print("".join(("#" if (x, y) in dots else " " for x in range(mx))))


dots = fold(dots, folds[1:])
# Part 2
grid(dots)
