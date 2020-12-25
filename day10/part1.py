import os
def get_input():
    return  [int(l.strip('\n')) for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

lines = sorted(get_input())
# add device's built in
lines.append(lines[-1] + 3)

prev = 0
count = [0, 0, 0, 0]

for n in lines:
    diff = n - prev
    count[diff] += 1
    prev = n

print(count[1] * count[3])
