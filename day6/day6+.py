races = [(46857582, 208141212571410)]
out = 1
for race in races:
    wins = 0
    t = race[0]
    d = race[1]
    for x in range(t+1): # Can optimise by direct calculation of x cutoff
        if x * (t - x) > d:
            wins += 1
    out *= wins
print(out)