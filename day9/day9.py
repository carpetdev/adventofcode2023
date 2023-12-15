with open('input.txt') as f:
    sequences = [[int(n) for n in sequence.split()] for sequence in f.read().splitlines()]

out = 0
for sequence in sequences:
    tower = [sequence]
    while not all(n == 0 for n in tower[-1]):
        tower.append([b - a for a, b in zip(tower[-1], tower[-1][1:])])
    tower[-1].append(0)
    while len(tower) > 1:
        diff = tower.pop().pop()
        tower[-1].append(tower[-1][-1] + diff)
    out += tower[-1][-1]

print(out)