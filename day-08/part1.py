import os
import re
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

visited = set()
cur = 0

intepreter = {
    'acc': lambda cur, acc, op: (cur + 1, acc + op),
    'jmp': lambda cur, acc, op: (cur + op, acc),
    'nop': lambda cur, acc, op: (cur + 1, acc)
}

lines = get_input()
accumulator = 0
while cur not in visited:
    visited.add(cur)

    cmd = lines[cur].split()[0]
    cur, accumulator = intepreter[cmd](
        cur,
        accumulator,
        int(lines[cur].split()[1])
    )

    if cur == len(lines):
        break

print(accumulator)
