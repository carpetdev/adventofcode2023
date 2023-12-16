from collections import defaultdict

with open('input.txt') as f:
    cave = f.read().splitlines()

pathses = []
for i in range(len(cave)):
    pathses.append([((i, 0), (0, 1))])
    pathses.append([((i, len(cave[0])-1), (0, -1))])
for j in range(len(cave[0])):
    pathses.append([((0, j), (1, 0))])
    pathses.append([((len(cave)-1, j), (-1, 0))])

out = 0
for paths in pathses:
    visited = defaultdict(list)
    while paths:
        (y, x), (dy, dx) = paths.pop()
        while 0 <= y < len(cave) and 0 <= x < len(cave[0]) and (dy, dx) not in visited[(y, x)]:
            visited[(y, x)].append((dy, dx))
            terrain = cave[y][x]
            if terrain == '\\':
                dy, dx = dx, dy
            elif terrain == '/':
                dy, dx = -dx, -dy
            elif (terrain == '-' and dy) or (terrain == '|' and dx):
                visited[(y, x)].append((-dy, -dx))
                dy, dx = dx, dy
                paths.append(((y, x), (-dy, -dx)))
            y += dy
            x += dx
    out = max(out, sum(1 for tile in visited if visited[tile]))

print(out)
# Optimise by memoising?!!!