out = 0
with open('input.txt') as f:
    while l := f.readline().rstrip().split():
        lookup = {'red': 0,
                  'green': 0,
                  'blue': 0}
        for n, c in zip(l[2::2], l[3::2]):
            lookup[c.rstrip(',;')] = max(lookup[c.rstrip(',;')], int(n))
        out += lookup['red'] * lookup['green'] * lookup['blue']
print(out)