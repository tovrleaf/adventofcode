lines = list(map(str.strip, open("input.txt").readlines()))
width = len(lines[0])

# Part 1
def most_common(data):
    return max(set(data), key=data.count)

bits = ""
for i in range(width):
    bits += str(most_common([int(x[i]) for x in lines]))

g = int(bits, 2)
e = int(''.join([str(1 if x == "0" else 0) for x in bits]), 2)

print(g * e)

# Part 2
generator, scrubber = [*lines], [*lines]
for i in range(width):
    g_common = int(sum([int(x[i]) for x in generator]) >= len(generator) / 2)
    generator = [x for x in generator if int(x[i]) == g_common] or generator

    s_common = int(sum([int(x[i]) for x in scrubber]) < len(scrubber) / 2)
    scrubber = [x for x in scrubber if int(x[i]) == s_common] or scrubber

o = int(generator.pop(), 2)
c = int(scrubber.pop(), 2)

print(o * c)
