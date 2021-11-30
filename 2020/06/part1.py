import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

groups = []
cur = ''
for l in get_input():
    cur += l
    if l == '':
        groups.append(cur)
        cur = ''
        continue
groups.append(cur)

lengths = [len(''.join(set(list(l)))) for l in groups]
print(sum(lengths))
