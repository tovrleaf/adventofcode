import os
def get_input():
    return  [int(l.strip('\n')) for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

lines = sorted(get_input())

# min difference is 1
count = {0: 1}
for n in lines:
    # start a new arrangement for charging
    count[n] = 0
    for i in range(1, 4):
        # if we can find a difference between 1-3 from count,
        # append all possible permutation to this voltage
        if n - i in count:
            count[n] += count[n - i]

print(count[max(lines)])
