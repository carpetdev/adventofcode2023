with open('input.txt') as f:
    platform = f.read().splitlines()

loads = [len(platform)] * len(platform[0])
out = 0
for i in range(len(platform)):
    for j in range(len(platform[i])):
        if platform[i][j] == 'O':
            out += loads[j]
            loads[j] -= 1
        elif platform[i][j] == '#':
            loads[j] = len(platform) - i - 1

print(out)

