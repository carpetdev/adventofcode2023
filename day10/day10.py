lookup = {'|': ((-1, 0), (1, 0)),
          '-': ((0, -1), (0, 1)),
          'L': ((-1, 0), (0, 1)),
          'J': ((-1, 0), (0, -1)),
          '7': ((1, 0), (0, -1)),
          'F': ((1, 0), (0, 1)),
          '.': (), 'S': ()}

with open('input.txt') as f:
    grid = f.read().splitlines()

tile = next((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S')
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        if (-i, -j) in lookup[grid[tile[0] + i][tile[1] + j]]:
            prev = tile
            tile = (tile[0] + i, tile[1] + j)
            break
    else:
        continue
    break

steps = 1
while grid[tile[0]][tile[1]] != 'S':
    neighbours = ((tile[0] + i, tile[1] + j) for i, j in lookup[grid[tile[0]][tile[1]]])
    new = next((x, y) for x, y in neighbours if (x, y) != prev)
    prev = tile
    tile = new
    steps += 1

print(steps//2)