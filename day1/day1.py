out = 0
with open('input.txt') as f:
    while l := f.readline().rstrip():
        d1 = None
        for c in l:
            if c.isdecimal():
                if not d1:
                    d1 = c
                d2 = c
        out += int(d1+d2)
print(out)