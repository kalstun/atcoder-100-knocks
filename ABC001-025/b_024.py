n,t = map(int, input().split())
a = [int(input()) for _ in range(n)]
r = 0
s = -100000
for i in a:
    r += t - max(0, s+t-i)
    s = i
else:
    print(r)
