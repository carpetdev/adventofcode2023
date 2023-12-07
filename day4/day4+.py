m = []
with open('input.txt') as f:
    while l := f.readline().rstrip().split():
        win = set()
        i = 2
        while l[i] != '|':
            win.add(int(l[i]))
            i += 1
        i += 1
        matches = 0
        while i < len(l):
            if int(l[i]) in win:
                matches += 1
            i += 1
        m.append(matches)
n = [1] * len(m)
for i in range(len(m)-1, -1, -1):
    for j in range(1, m[i]+1):
        n[i] += n[i+j]
print(sum(n))