import os

def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

valid_count = 0

for line in get_input():
    rules, password = line.split(': ')
    boundaries, char = rules.split(' ')
    low, high = [int(b) for b in boundaries.split('-')]

    if low <= password.count(char) <= high:
        valid_count += 1

print(valid_count)
