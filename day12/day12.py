def arrangements(s, i, p, d):
    if d > sum(p):
        return False

    if sum(1 for c in s if c != '.') < sum(p):
        return False

    if i == len(s):
        q = [0]
        for c in s:
            if c == '.':
                q.append(0)
            else:
                q[-1] += 1
        q = list(filter(None, q))
        if q == p:
            return True
        return False

    if s[i] == '?':
        return arrangements(s[:i] + '.' + s[i+1:], i+1, p, d) + arrangements(s[:i] + '#' + s[i+1:], i+1, p, d+1)
    elif s[i] == '#':
        return arrangements(s, i+1, p, d+1)
    return arrangements(s, i+1, p, d)

with open('input.txt') as f:
    lines = f.read().splitlines()

out = 0
for line in lines:
    s, p = line.split()
    p = [int(n) for n in p.split(',')]
    out += arrangements(s, 0, p, 0)

print(out)