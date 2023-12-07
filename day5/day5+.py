with open('input.txt') as f:
    almanac = f.read().rstrip().split('\n\n')

seeds = list(map(int, almanac[0].split()[1:]))
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

for level in almanac[1:]:
    maps = level.split('\n')[1:]
    locations = []
    for seed in seeds:
        mapped = []
        for m in maps:
            m = m.split()
            if seed[0] < int(m[1]) + int(m[2]) and int(m[1]) < seed[0] + seed[1]:
                 mapped.append((max(seed[0], int(m[1])),
                        min(seed[0] + seed[1], int(m[1]) + int(m[2])) - max(seed[0], int(m[1]))))
                 locations.append((int(m[0]) + mapped[-1][0] - int(m[1]), mapped[-1][1]))
        mapped.sort()
        start = prev_end = seed[0]
        length = 0
        for start, length in mapped:
            if start > prev_end + 1:
                locations.append((prev_end, start - prev_end))
            prev_end = start + length - 1
        if start + length < seed[0] + seed[1]:
            locations.append((start + length, seed[0] + seed[1] - start - length))
    seeds = locations

print(min(locations)[0])