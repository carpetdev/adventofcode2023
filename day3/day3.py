lookup = set()
with open('input.txt') as f:
    r = 0
    while l := f.readline().rstrip():
        for c in range(len(l)):
            if not l[c].isdecimal() and l[c] != '.':
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        lookup.add((r+i,c+j))
        r += 1
out = 0
with open('input.txt') as f:
    r = 0
    while l := f.readline().rstrip():
        l += '.'
        num = ''
        for c in range(len(l)):
            if l[c].isdecimal():
                num += l[c]
            else:
                if num and (lookup & {(r,c-i-1) for i in range(len(num))}):
                    out += int(num)
                num = ''
        r += 1
print(out)