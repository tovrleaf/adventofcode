data = list(map(str.strip, open("input.txt").readlines()))

# Part 1
print(sum(map(len, map(list, [filter(lambda x: x in [2, 3, 4, 7], map(len, line.split(" | ")[1].split())) for line in data]))))

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#$
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def by_length(data, length):
    return (set(x) for x in data if len(x) == length)

total = 0
for line in data:
    inp, outp = line.split(' | ')
    inp = inp.split()

    digits = [set()] * 10
    digits[1] = next(by_length(inp, 2))
    digits[4] = next(by_length(inp, 4))
    digits[7] = next(by_length(inp, 3))
    digits[8] = next(by_length(inp, 7))

    maybe235  = by_length(inp, 5)
    for maybe in maybe235:
        if digits[1].issubset(maybe):
            digits[3] = maybe
        elif len(digits[4] & maybe) == 3:
            digits[5] = maybe
        else:
            digits[2] = maybe

    maybe069 = by_length(inp, 6)
    for maybe in maybe069:
       if len(maybe & digits[4]) == 4:
           digits[9] = maybe
       elif len(maybe & digits[5]) == 5:
           digits[6] = maybe
       else:
           digits[0] = maybe

    value = ""
    for out in outp.split():
        value += str(digits.index(set(out)))
    total += int(value)

# Part 2
print(total)
