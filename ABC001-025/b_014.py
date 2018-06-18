n,x = map(int, input().split())
a = list(map(int, input().split()))
s = 0
bx = bin(x)
for i in range(len(bx)-2):
    if bx[-i-1] == "1":
        s += a[i]
    else:
        continue
else:
    print(s)
