with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0]
lookup = {}
for line in lines[2:]:
    lookup[line[:3]] = (line[7:10], line[12: 15])
node = 'AAA'
i = 0
while node != 'ZZZ':
    if instructions[i % len(instructions)] == 'L':
        node = lookup[node][0]
    else:
        node = lookup[node][1]
    i += 1
print(i)