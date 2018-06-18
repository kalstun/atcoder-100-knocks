n,s,t = map(int, input().split())
w = int(input())
if w >= s and w <= t:
    b = 1
else:
    b = 0

for _ in range(n-1):
    a = int(input())
    w += a
    if w >= s and w <= t:
        b += 1

else:
    print(b)
