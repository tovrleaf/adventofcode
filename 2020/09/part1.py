import os
def get_input():
    return  [int(l.strip('\n')) for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

lines = get_input()

p = 25
prev = lines[:p]
for n in lines[p:]:
    found = False
    for s in [i for i in prev if i <= n]:
        if n - s in prev:
            found = True
            break
    if not found:
        print(n)
        break
    prev = prev[1:] + [n]
