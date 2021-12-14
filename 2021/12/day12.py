data = [x.split("-") for x in map(str.strip, open("input.txt").readlines())]

graph = {}
for orig, dest in data:
    for x in [orig, dest]:
        if x not in graph:
            graph[x] = set()
    graph[orig].add(dest)
    graph[dest].add(orig)

def find_paths(graph, key, seen = [], repeat = 1):
    if key == "end":
        return 1

    length = 0
    for node in graph[key]:
        if node == "start":
            continue

        if node.isupper() or node not in seen:
            length += find_paths(graph, node, seen + [node], repeat)
        elif node.islower() and repeat > 1:
            length += find_paths(graph, node, seen, repeat - 1)
    return length

# Part 1
print(find_paths(graph, "start"))
# Part 2
print(find_paths(graph, "start", repeat = 2))
