with open('input.txt') as f:
    sky = f.read().splitlines()

empty_rows = [i for i in range(len(sky)) if '#' not in sky[i]]
empty_columns = [j for j in range(len(sky[0])) if not any(sky[i][j] == '#' for i in range(len(sky)))]

for i in range(len(empty_rows)):
    sky.insert(i + empty_rows[i], '.' * len(sky[0]))

for j in range(len(empty_columns)):
    sky = [row[:j + empty_columns[j]] + '.' + row[j + empty_columns[j]:] for row in sky]

galaxies = []
for i in range(len(sky)):
    for j in range(len(sky[0])):
        if sky[i][j] == '#':
            galaxies.append((i, j))

out = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        out += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(out)