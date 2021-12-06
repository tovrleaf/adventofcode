line = list(map(int, open("input.txt").readline().split(",")))

data = dict.fromkeys(range(9), 0)
for i in line:
    data[i] += 1

def days(d, data):
    for _ in range(d):
        new = data[0]
        for k, v in dict(list(data.items())[1:9]).items():
            data[k - 1] = v

        data[6] += new
        data[8] = new
    return sum(data.values())

# Part 1
print(days(80, data.copy()))
# Part 2
print(days(256, data.copy()))
