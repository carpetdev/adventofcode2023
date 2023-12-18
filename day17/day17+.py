from heapq import *

with open('input.txt') as f:
    heats = f.read().splitlines()

layers = 10
min_turn = 4
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
distances = [[[[float('inf')] * layers for _ in range(4)] for _ in range(len(heats[0]))] for _ in range(len(heats))]
parents = [[[[None] * layers for _ in range(4)] for _ in range(len(heats[0]))] for _ in range(len(heats))]
q = [(0, (0, 0, 0, 0))]

while (node_data := heappop(q))[1][:2] != (len(heats)-1, len(heats[0])-1):
    distance, (y, x, d, z) = node_data
    for e, (i, j) in enumerate(directions):
            k = z - 1 if e == d else layers - 1
            if 0 <= y+i < len(heats) and 0 <= x+j < len(heats[0]) and abs(e - d) != 2 and k >= 0:
                if e != d and z > layers - min_turn:
                    continue
                # if y+i == len(heats)-1 and x+j == len(heats[0])-1 and k > layers - min_turn:
                #     continue
                if distance + int(heats[y+i][x+j]) < distances[y+i][x+j][e][k]:
                    distances[y+i][x+j][e][k] = distance + int(heats[y+i][x+j])
                    parents[y+i][x+j][e][k] = (y, x, d, z)
                    heappush(q, (distances[y+i][x+j][e][k], (y+i, x+j, e, k)))

# # Printing path for debugging
ans = min(min(x for x in distances[-1][-1]))
node = next((len(heats)-1, len(heats[0])-1, d, z) for d in range(4) for z in range(layers) if distances[-1][-1][d][z] == ans)
pics = ('^', '>', 'v', '<')
while node[:2] != (0, 0):
    # print(node)
    heats[node[0]] = heats[node[0]][:node[1]] + pics[node[2]] + heats[node[0]][node[1]+1:]
    node = parents[node[0]][node[1]][node[2]][node[3]]
print('\n'.join(heats))
print(ans)