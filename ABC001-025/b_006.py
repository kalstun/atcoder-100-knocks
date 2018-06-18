n = int(input())
t = [0,0,1]
if n <= 3:
    print(t[n-1])
else:
    for _ in range(n-3):
        s = sum(t) % 10007
        t = [t[1], t[2], s]
    else:
        print(t[-1])
