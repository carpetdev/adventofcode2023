from collections import defaultdict
from functools import reduce
import operator
lookup = defaultdict(set)
with open('input.txt') as f:
    engine = [f'.{row}.' for row in f.read().splitlines()]
for r in range(len(engine)):
    for c in range(len(engine[0])):
        if engine[r][c] == '*':
           for (x,y) in ((r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1),
                        (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)):
                i = j = y
                while engine[x][i].isdecimal(): # Lucky no *'s at edges
                    i -= 1
                while engine[x][j].isdecimal():
                    j += 1
                if i == j:
                    continue
                lookup[(r,c)].add((x, i, int(engine[x][i+1:j])))
out = sum(reduce(operator.mul, (num[2] for num in nums), 1) for nums in lookup.values() if len(nums) == 2)
print(out)