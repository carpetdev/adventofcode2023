from math import lcm

def main():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    instructions = lines[0]
    lookup = {}
    for line in lines[2:]:
        lookup[line[:3]] = (line[7:10], line[12: 15])
    nodes = list(lookup.keys())
    next_node = [None] * len(nodes)
    finishes = [[] for _ in range(len(nodes))]
    for i in range(len(nodes)):
        node = nodes[i]
        for j in range(len(instructions)):
            if instructions[j] == 'L':
                node = lookup[node][0]
            else:
                node = lookup[node][1]
            if node[2] == 'Z':
                finishes[i].append(j+1)
        next_node[i] = node
##    print(finishes)
##    print(len(instructions)) ## Conclude that each node is reached by repeating blocks of all the instructions

    starts = [node for node in nodes if node[2] == 'A']
    out = 1
    for start in starts:
        i = 0
        while start[2] != 'Z':
            i += 1
            start = next_node[nodes.index(start)]
        out = lcm(out, i)
    return out * len(instructions)

print(main())

