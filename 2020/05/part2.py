import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

def to_int(table, string):
    trans_table = string.maketrans(table, '01')
    return int(string.translate(trans_table), 2)

rows = [to_int("FB", l[:7]) for l in get_input()]
cols = [to_int("LR", l[7:]) for l in get_input()]

seats = zip(rows, cols)
ids = [x[0] * 8 + x[1] for x in seats]

for i in range(max(ids)):
    l = i - 1
    r = i + 1
    if l in ids and r in ids and i not in ids:
        print(i)
        break

