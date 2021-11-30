import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

orientation = ['N', 'E', 'S', 'W']
direction = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
turn = {'L': -1, 'R': 1}

coord = (0, 0)
facing = 'E'

def move(coord, key, val):
    return (
        coord[0] + direction[key][0] * val,
        coord[1] + direction[key][1] * val)

for line in get_input():
    cmd = line[0]
    val = int(line[1:])
    if cmd in direction:
        coord = move(coord, cmd, val)
    elif cmd in turn:
        # turn 180 into 2 etc
        rotate = (val // 90) * turn[cmd]
        facing = orientation[(orientation.index(facing) + rotate) % 4]
    elif cmd == 'F':
        coord = move(coord, facing, val)

print(abs(coord[0]) + abs(coord[1]))
