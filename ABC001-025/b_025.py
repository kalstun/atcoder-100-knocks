n,a,b = map(int, input().split())
c = []
for _ in range(n):
    s,d = input().split()
    d = max(a, min(b, int(d)))
    if s == "West":
        c.append(-d)
    else:
        c.append(d)
else:
    t = sum(c)
    if t < 0:
        print("West", abs(t))
    elif t > 0:
        print("East", t)
    else:
        print(0)
