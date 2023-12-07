out = 0
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
        if matches > 0:
            out += 2**(matches-1)
print(out)