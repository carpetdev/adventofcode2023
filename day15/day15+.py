with open('input.txt') as f:
    sequence = f.read().strip().split(',')

boxes = [{} for _ in range(256)]
for s in sequence:
    label = ''
    hash = 0
    for c in s:
        if c == '=':
            boxes[hash][label] = int(s[-1])
            break
        elif c == '-':
            boxes[hash].pop(label, None)
        else:
            label += c
            hash += ord(c)
            hash *= 17
            hash %= 256

out = 0
for i, d in enumerate(boxes, 1):
    for j, (_, f) in enumerate(d.items(), 1):
        out += i * j * f

print(out)