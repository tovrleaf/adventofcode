import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

def to_int(table, string):
    trans_table = string.maketrans(table, '01')
    return int(string.translate(trans_table), 2)

rows = [to_int("FB", l[:7]) for l in get_input()]
max_value = max(rows)
max_index = rows.index(max_value)

cols = [to_int("LR", l[7:]) for l in get_input()]

print(max_value * 8 + cols[max_index])
