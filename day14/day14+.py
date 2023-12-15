from copy import deepcopy

with open('input.txt') as f:
    platform = [list(line) for line in f.read().splitlines()]

def tilt_up(platform):
    heights = [0] * len(platform[0])
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                platform[i][j], platform[heights[j]][j] = platform[heights[j]][j], platform[i][j]
                heights[j] += 1
            elif platform[i][j] == '#':
                heights[j] = i+1

prevs = []
i = 0
while True:
    prevs.append(deepcopy(platform))
    tilt_up(platform)
    platform = [list(row) for row in zip(*reversed(platform))]
    tilt_up(platform)
    platform = [list(row) for row in zip(*reversed(platform))]
    tilt_up(platform)
    platform = [list(row) for row in zip(*reversed(platform))]
    tilt_up(platform)
    platform = [list(row) for row in zip(*reversed(platform))]
    i += 1
    if platform in prevs:
        s = prevs.index(platform)
        platform = prevs[s + (1000000000 - s) % (i - s)]
        break

print(sum((len(platform)-i) * platform[i].count('O') for i in range(len(platform))))
