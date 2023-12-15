with open('input.txt') as f:
    sequence = f.read().strip().split(',')

out = 0
for s in sequence:
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    out += val

print(out)