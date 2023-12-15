with open('input.txt') as f:
    sky = f.read().splitlines()

empty_rows = [i for i in range(len(sky)) if '#' not in sky[i]]
empty_columns = [j for j in range(len(sky[0])) if not any(sky[i][j] == '#' for i in range(len(sky)))]

galaxies = []
for i in range(len(sky)):
    for j in range(len(sky[0])):
        if sky[i][j] == '#':
            galaxies.append((i, j))

out = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        x1 = min(galaxies[i][0], galaxies[j][0])
        x2 = max(galaxies[i][0], galaxies[j][0])
        y1 = min(galaxies[i][1], galaxies[j][1])
        y2 = max(galaxies[i][1], galaxies[j][1])
        out += x2 - x1 + y2 - y1
        out += sum(999999 for row in empty_rows if x1 <= row <= x2)
        out += sum(999999 for col in empty_columns if y1 <= col <= y2)

print(out)