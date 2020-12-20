import os
import re
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

p = r'^(.+) bags contain (.+)\.$'
outer = {}
for l in get_input():
    m = re.search(p, l)
    outer[m.group(1)] = set()
    for b in m.group(2).split(', '):
        if b != 'no other bags':
            outer[m.group(1)].add(' '.join(b.split()[1:3]))

def find_bag(color):
    count = 0
    bag = outer[color]
    if len(bag) == 0:
        return count
    for subcolor in bag:
        if subcolor == 'shiny gold':
            count += 1
        count += find_bag(subcolor)
    return count

print(len(list(filter(lambda x: find_bag(x) > 0, outer.keys()))))
