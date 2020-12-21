import os
import re
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

p = r'^(.+) bags contain (.+)\.$'
outer = {}
for l in get_input():
    m = re.search(p, l)
    outer[m.group(1)] = {}
    for b in m.group(2).split(', '):
        if b != 'no other bags':
            outer[m.group(1)][' ' .join(b.split()[1:3])] = b.split()[0]

def find_bag(color):
    count = 0
    color_collection = outer[color]
    if len(color_collection) == 0:
        return count
    for cur_color in color_collection:
        cur_count = int(color_collection[cur_color])
        count += cur_count + cur_count * find_bag(cur_color)
    return count

print(find_bag('shiny gold'))
