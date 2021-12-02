lines = list(map(str.strip, open("input.txt").readlines()))

# Part 1
y, h = 0, 0

for line in lines:
    c, x = line.split()
    x = int(x)
    if c == "forward":
        y += x
    else:
        h += {"up": -1, "down": 1}[c] * x

print(y * h)

# Part 2
y, h, aim = 0, 0, 0

for line in lines:
    c, x = line.split()
    x = int(x)
    if c == "forward":
        y += x
        h += x * aim
    else:
        aim += {"up": -1, "down": 1}[c] * x

print(y * h)
