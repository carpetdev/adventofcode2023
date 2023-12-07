with open('input.txt') as f:
    almanac = f.read().rstrip().split('\n\n')

seeds = list(map(int, almanac[0].split()[1:]))
for level in almanac[1:]:
    locations = [None] * len(seeds)
    maps = level.split('\n')[1:]
    for m in maps:
        m = m.split()
        for i in range(len(seeds)):
            if 0 <= seeds[i] - int(m[1]) < int(m[2]):
                locations[i] = int(m[0]) + seeds[i] - int(m[1])
    locations = [locations[i] if locations[i] is not None else seeds[i] for i in range(len(seeds))]
    seeds = locations

print(min(locations))