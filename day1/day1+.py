lookup = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9'}
out = 0
with open('input.txt') as f:
    while l := f.readline().rstrip():
        d1 = None
        for i, c in enumerate(l):
            if c.isdecimal():
                x = c
            else:
                x = lookup.get(l[i:i+3], None) or lookup.get(l[i:i+4], None) or lookup.get(l[i:i+5], None)
            if x:
                if not d1:
                    d1 = x
                d2 = x
        out += int(d1+d2)
print(out)