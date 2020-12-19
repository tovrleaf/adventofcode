import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

groups = []
subgroups = []
for l in get_input():
    if l == '':
        groups.append(subgroups)
        subgroups = []
        continue
    subgroups.append(l)
groups.append(subgroups)

intersects = [set.intersection(*[set(set(g)) for g in group]) for group in groups]
print(sum(map(len, intersects)))
