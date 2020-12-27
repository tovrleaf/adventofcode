import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

orientation = ['N', 'E', 'S', 'W']
direction = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
turn = {'L': (-1, 1), 'R': (1, -1)}

coord = (0, 0)
way_coord = (10, 1)

def move(coord, key, val):
    return (
        coord[0] + direction[key][0] * val,
        coord[1] + direction[key][1] * val)

for line in get_input():
    cmd = line[0]
    val = int(line[1:])
    if cmd in direction:
        way_coord = move(way_coord, cmd, val)
    elif cmd in turn:
        for i in range(val // 90):
            way_coord = (
                    way_coord[1] * turn[cmd][0],
                    way_coord[0] * turn[cmd][1])
    elif cmd == 'F':
        coord = (coord[0] + way_coord[0] * val, coord[1] + way_coord[1] * val)

print(abs(coord[0]) + abs(coord[1]))
