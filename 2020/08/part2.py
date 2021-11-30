import os
import re
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

intepreter = {
    'acc': lambda cur, acc, op: (cur + 1, acc + op),
    'jmp': lambda cur, acc, op: (cur + op, acc),
    'nop': lambda cur, acc, op: (cur + 1, acc)
}

def traverse(lines):
    visited = set()
    cur = 0
    accumulator = 0
    last_line = False

    while cur not in visited:
        visited.add(cur)

        cmd = lines[cur].split()[0]
        cur, accumulator = intepreter[cmd](
            cur,
            accumulator,
            int(lines[cur].split()[1])
        )

        if cur == len(lines):
            return accumulator, True

    return accumulator, False

lines = get_input()
acc = 0
for i in range(len(lines)):
    local_lines = lines.copy()

    if 'jmp' == local_lines[i].split()[0]:
        local_lines[i] = 'nop ' + local_lines[i].split()[1]
    elif 'nop' == local_lines[i].split()[0]:
        local_lines[i] = 'jmp ' + local_lines[i].split()[1]

    acc, trough = traverse(local_lines)
    if trough:
        break

print(acc)




