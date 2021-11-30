import os

def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

def travel(right, down):
    data = get_input()
    x = 0
    y = 0
    trees = 0
    for i in range(len(data)):
        if i % down != 0:
            continue
        if data[i][x] == '#':
            trees += 1
        x = (x + right) % len(data[0])
    return trees

total = 1
for r, d in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    total *= travel(r, d)

print(total)
