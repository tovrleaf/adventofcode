import os
import sys

def get_input():
    return  [int(l.strip('\n')) for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt']    )).readlines()]

items = get_input()

for i in items:
    for j in items:
        for k in items:
            if i + j + k == 2020:
                print(i * j * k)
                sys.exit(0)
