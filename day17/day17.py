from heapq import *

with open('input.txt') as f:
    heats = f.read().splitlines()

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
distances = [[[[float('inf')] * 3 for _ in range(4)] for _ in range(len(heats[0]))] for _ in range(len(heats))]
parents = [[[[None] * 3 for _ in range(4)] for _ in range(len(heats[0]))] for _ in range(len(heats))]
q = [(0, (0, 0, 0, 0))]

while (node_data := heappop(q))[1][:2] != (len(heats)-1, len(heats[0])-1):
    distance, (y, x, d, z) = node_data
    # # Premature optimisation :)
    # if distance > distances[y][x][d][z]:
    #     continue
    for e, (i, j) in enumerate(directions):
        # This loop is silly! Only want the maximum possible k value
        for k in range(z if e == d else 3):
            if 0 <= y+i < len(heats) and 0 <= x+j < len(heats[0]) and abs(e - d) != 2:
                if distance + int(heats[y+i][x+j]) < distances[y+i][x+j][e][k]:
                    distances[y+i][x+j][e][k] = distance + int(heats[y+i][x+j])
                    parents[y+i][x+j][e][k] = (y, x, d, z)
                    heappush(q, (distances[y+i][x+j][e][k], (y+i, x+j, e, k)))

# # Printing path for debugging
ans = min(min(x for x in distances[-1][-1]))
# node = next((len(heats)-1, len(heats[0])-1, d, z) for d in range(4) for z in range(3) if distances[-1][-1][d][z] == ans)
# pics = ('^', '>', 'v', '<')
# while node[:2] != (0, 0):
#     print(node)
#     heats[node[0]] = heats[node[0]][:node[1]] + pics[node[2]] + heats[node[0]][node[1]+1:]
#     node = parents[node[0]][node[1]][node[2]][node[3]]
# print('\n'.join(heats))
print(ans)