import os
import sys

def get_input():
    return  [int(l.strip('\n')) for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt']    )).readlines()]

items = get_input()

for i in items:
    for j in items:
        if i + j == 2020:
            print(i * j)
            sys.exit(0)
