from functools import cache

@cache
def arrangements(s, p):
    if sum(c != '.' for c in s) < sum(p):
        return False

    if p == ():
        return all(c != '#' for c in s)

    if s[0] == '.':
        return arrangements(s[1:], p)
    elif s[0] == '#':
        if all(c != '.' for c in s[:p[0]]):
            if len(s) == p[0]:
                return len(p) == 1
            if s[p[0]] != '#':
                return arrangements(s[p[0]+1:], p[1:])
            return False
        return False
    else:
        return arrangements('.' + s[1:], p) + arrangements('#' + s[1:], p)

with open('input.txt') as f:
    lines = f.read().splitlines()

out = 0
for line in lines:
    s, p = line.split()
    s = '?'.join([s] * 5)
    p = [int(n) for n in p.split(',')] * 5
    out += arrangements(s, tuple(p))

print(out)