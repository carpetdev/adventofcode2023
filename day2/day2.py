lookup = {'red': 12,
          'green': 13,
          'blue': 14}
out = 5050
with open('input.txt') as f:
    while l := f.readline().rstrip().split():
        id = int(l[1][:-1])
        for n, c in zip(l[2::2], l[3::2]):
            if int(n) > lookup[c.rstrip(',;')]:
                out -= id
                break
print(out)