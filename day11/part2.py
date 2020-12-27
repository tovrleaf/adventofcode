import os
def get_input():
    return  [l.strip('\n') for l in open('/'.join([os.path.dirname(os.path.abspath(__file__)), 'input.txt'])).readlines()]

adjanced = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
lines = get_input()

def occupied(x, y, rows):
    count = 0
    w, h = len(lines), len(lines[0])
    for i, j in adjanced:
        xi = x + i
        yj = y + j
        while 0 <= xi < w and 0 <= yj < h:
            if rows[xi][yj] == 'L':
                break
            if rows[xi][yj] == '#':
                count += 1
                break
            xi += i
            yj += j
    return count

def change_char(line, i, char):
    return line[:i] + char + line[i + 1:]

def rules(layout):
    prev_layout = layout.copy()
    while True:
        for row, row_data in enumerate(layout):
            for col, col_data in enumerate(row_data):
                num = occupied(row, col, prev_layout)
                if num == 0 and col_data == 'L':
                    layout[row] = change_char(layout[row], col, '#')
                elif num >= 5 and col_data == '#':
                    layout[row] = change_char(layout[row], col, 'L')

        if prev_layout == layout:
            break
        prev_layout = layout.copy()

    return layout

print(sum([x.count('#') for x in rules(lines)]))
