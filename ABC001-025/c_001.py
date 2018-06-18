BEAUFORT_SCALE = (0, 0.25, 1.55, 3.35, 5.45, 7.95, 10.75, 13.85, 17.15, 20.75, 24.45, 28.45, 32.65)
DIRECTION = ("N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N")

deg,dis = map(int, input().split())

for bfs in BEAUFORT_SCALE[::-1]:
    if dis >= bfs * 60:
        w = BEAUFORT_SCALE.index(bfs)
        break

if w == 0:
    dir = "C"
else:
    dir = DIRECTION[(deg+112)//225]

print(dir, w)
