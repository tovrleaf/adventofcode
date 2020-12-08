import os

def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

x = 0
trees = 0

for l in get_input():
    if l[x] == '#':
        trees += 1
    x = (x + 3) % len(l)

print(trees)
