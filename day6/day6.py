races = [(46, 208), (85, 1412), (75, 1257), (82, 1410)]
out = 1
for race in races:
    wins = 0
    t = race[0]
    d = race[1]
    for x in range(t+1):
        if x * (t - x) > d:
            wins += 1
    out *= wins
print(out)