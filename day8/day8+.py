with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0]
lookup = {}
for line in lines[2:]:
    lookup[line[:3]] = (line[7:10], line[12: 15])
nodes = [node for node in lookup if node[2] == 'A']
i = 0
while not all(node[2] == 'Z' for node in nodes):
    if instructions[i % len(instructions)] == 'L':
        nodes = [lookup[node][0] for node in nodes]
    else:
        nodes = [lookup[node][1] for node in nodes]
    i += 1
print(i)