with open('input.txt') as f:
    patterns = [pattern.splitlines() for pattern in f.read().split('\n\n')]

def find_horz_mirror(pattern):
    N = len(pattern) - 2 if len(pattern) % 2 else len(pattern) - 1
    for i in range(N, 0, -2):
        if pattern[0] == pattern[i]:
            for j in range(1, (i+1)//2):
                if pattern[j] != pattern[i-j]:
                    break
            else:
                return (i+1)//2
    return None

out = 0
for pattern in patterns:
    if (mirror := find_horz_mirror(pattern)) is not None:
        out += mirror * 100
    elif (mirror := find_horz_mirror(pattern[::-1])) is not None:
        out += (len(pattern) - mirror) * 100
    elif (mirror := find_horz_mirror([''.join(col) for col in zip(*pattern)])) is not None:
        out += mirror
    elif (mirror := find_horz_mirror([''.join(col) for col in zip(*pattern)][::-1])) is not None:
        out += len(pattern[0]) - mirror
    else:
        print('no mirror')

print(out)