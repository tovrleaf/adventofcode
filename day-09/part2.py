import os
import sys
def get_input():
    return  [int(l.strip('\n')) for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

def invalid_number(lines, preamble):
    prev = lines[:preamble]
    for n in lines[preamble:]:
        found = False
        for s in [i for i in prev if i <= n]:
            if n - s in prev:
                found = True
                break
        if not found:
            # invalid number
            return n
        prev = prev[1:] + [n]

lines = get_input()
needle = invalid_number(lines, 25)

range_sum = 0
range_window = []
for n in lines:
    range_sum += n
    range_window += [n]
    while range_sum > needle:
        range_sum -= range_window[0]
        range_window = range_window[1:]
    if range_sum == needle:
        print(min(range_window) + max(range_window))
        sys.exit(0)
